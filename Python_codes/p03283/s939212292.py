class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(self.n+1) # 1-indexed

    def init(self, init_val):
        for i, v in enumerate(init_val):
            self.add(i, v)

    def add(self, i, x):
        # i: 0-indexed
        i += 1 # to 1-indexed
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

    def sum(self, i, j):
        # return sum of [i, j)
        # i, j: 0-indexed
        return self._sum(j) - self._sum(i)

    def _sum(self, i):
        # return sum of [0, i)
        # i: 0-indexed
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & (-i)
        return res

import sys
import io, os
#input = sys.stdin.buffer.readline
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, m, Q = map(int, input().split())
X = []
A = []
for i in range(m):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    A.append(l)
    A.append(r)
    X.append((l, r, 0, i))
for i in range(Q):
    p, q = map(int, input().split())
    p, q = p-1, q-1
    A.append(p)
    A.append(q)
    X.append((p, q, 1, i))
X.sort(key=lambda x: (x[1], x[2]))

A = list(set(A))
A.sort()
d = {}
for i, a in enumerate(A):
    d[a] = i

bit = BIT(550)
ans = [-1]*Q
for l, r, t, i in X:
    l, r = d[l], d[r]
    if t == 0:
        bit.add(l, 1)
    else:
        ans[i] = bit.sum(l, r+1)
print(*ans, sep='\n')
