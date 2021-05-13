import bisect
n, d, a = map(int, input().split())
XH = sorted([list(map(int, input().split())) for _ in range(n)])
X, H = zip(*XH)
K = [-(-i//a) for i in H]
L = [0]*(n+2)
ans = 0
for i in range(n):
  L[i+1] += L[i]
  s = max(K[i]-L[i+1], 0)
  ans += s
  L[i+1] += s
  L[bisect.bisect_right(X, X[i]+2*d)+1] -= s
print(ans)
