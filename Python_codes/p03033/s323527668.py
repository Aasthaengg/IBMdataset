import sys
import bisect

sys.setrecursionlimit(10**8)

class SegmentTree(object):  #1-indexed
    def __init__(self, size, value):
        self.len = 1 << size.bit_length()
        self.default = value
        # print(self.len)
        self.array = [value] * (2 * self.len)

    def get(self, i):
        i += self.len
        ans = self.default
        while i > 0:
            ans = min(self.array[i], ans)
            i >>= 1
        return ans

    def query(self, l, r, v, i, a, b):
        if self.array[i] != self.default:
            return 0
        if l == a and r == b:
            self.array[i] = v
            return 0
        center = (a + b) // 2
        if center >= r:
            return self.query(l, r, v, i * 2, a, center)
        elif center <= l:
            return self.query(l, r, v, i * 2 + 1, center, b) 
        else:
            return min(
                self.query(l, center, v, i * 2, a, center),
                self.query(center, r, v, i * 2 + 1, center, b))

    def update(self, l, r, v):
        return self.query(l, r, v, 1, 0, self.len)


input = sys.stdin.readline

N, Q = map(int, input().split())

STX_array = [list(map(int, input().split())) for _ in range(N)]

STX_array = sorted(STX_array, key=lambda x: x[2])

Q_array = [int(input()) for _ in range(Q)]

index_array = [i for i in range(Q)]

INF = 10**9 + 7

seg_tree = SegmentTree(Q, INF)

for STX in STX_array:
    s, t, x = STX
    index_left = bisect.bisect_left(Q_array, s - 0.5 - x)
    index_right = bisect.bisect_left(Q_array, t - 0.5 - x)
    if index_left != index_right:
        seg_tree.update(index_left, index_right, x)

for i in range(Q):
    ans = seg_tree.get(i)
    print(ans) if ans != INF else print(-1)