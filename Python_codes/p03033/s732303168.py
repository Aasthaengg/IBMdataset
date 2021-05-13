import sys
import bisect
 
N, Q = map(int, input().split(' '))
G = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
T = [int(sys.stdin.readline()) for _ in range(Q)]

class SegTree :
    def __init__(self, n) :
        self.n = n
        self.A = [10**15] * (2 << (n + 1).bit_length())
 
    def update(self, l, r, val) :
      l += len(self.A) // 2
      r += len(self.A) // 2
      while l < r:
          if l & 1 :
              self.A[l] = min(self.A[l], val)
              l += 1
          if r & 1:
              self.A[r-1] = min(self.A[r-1], val)
              r -= 1
          l //= 2
          r //= 2

    def get(self, i) :
      i += len(self.A) // 2
      ret = self.A[i]
      while i > 0 :
          i //= 2
          ret = min(ret, self.A[i])
      return ret if ret < 10**15 else -1

ST = SegTree(Q)
for g in G :
    s = g[0] - g[2]
    e = g[1] - g[2]
 
    ll = bisect.bisect_left(T, s)
    rr = bisect.bisect_left(T, e)
 
    if ll == rr :
        continue
 
    ST.update(ll, rr, g[2])
 
for i in range(Q) :
    ans = ST.get(i)
    print(ans)
