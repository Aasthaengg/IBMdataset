import sys
input = lambda : sys.stdin.readline().rstrip()

def segfun(x, y):
    return min(x, y)
ide_ele = 10**9 + 1


class SegmentTree:
    def __init__(self, n, ele, segfun):
        self.ide_ele = ele
        self.segfun = segfun
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [self.ide_ele] * (self.N0 * 2)
 
    def update(self, l, r, val):
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] = self.segfun(self.data[l], val)
                l += 1
            if r & 1:
                self.data[r - 1] = self.segfun(self.data[r - 1], val)
                r -= 1
            l //= 2
            r //= 2
 
    def query(self, i):
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = self.segfun(ret, self.data[i])
        return ret


n, q = map(int, input().split())
stx = []
for _ in range(n):
    s, t, x = map(int, input().split())
    stx.append([x, s - x, t - x])
# stx.sort(reverse=True)
d = [int(input()) for _ in range(q)]

import bisect

seg = SegmentTree(q, ide_ele, segfun)

for x, start, last in stx:
    l = bisect.bisect_left(d, start)
    r = bisect.bisect_left(d, last)
    seg.update(l, r, x)

for i, j in enumerate(d):
    res = seg.query(i)
    if res == ide_ele:
        print(-1)
    else:
        print(res)
    

