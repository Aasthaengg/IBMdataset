import sys
import bisect


class DualSegmentTree():

    def __init__(self, n):
        INF = float("inf")
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.node = [INF] * (2*self.size - 1)

    def update(self, begin, end, val):
        begin += (self.size - 1)
        end += (self.size - 1)
        while begin < end:
            if (end - 1) & 1:
                end -= 1
                self.node[end] = min(val, self.node[end])
            if (begin - 1) & 1:
                self.node[begin] = min(val, self.node[begin])
                begin += 1
            begin = (begin - 1) // 2
            end = (end - 1) // 2

    def get_val(self, i):
        i += (self.size - 1)
        val = self.node[i]
        while i > 0:
            i = (i - 1) // 2
            val = min(val, self.node[i])
        return val

n, q = map(int, input().split())
info = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
d = [int(sys.stdin.readline()) for i in range(q)]
INF = float("inf")

st = DualSegmentTree(len(d)+1)

for i in range(n):
    a, b = info[i][0] - info[i][2], info[i][1] - info[i][2]  
    l = bisect.bisect_left(d, a)
    r = bisect.bisect_left(d, b)
    st.update(l, r, info[i][2])

for i in range(q):
    tmp = st.get_val(i)
    if tmp == float("inf"):
        print(-1)
    else:
        print(tmp)
