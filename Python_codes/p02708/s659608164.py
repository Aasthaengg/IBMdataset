def _sum(l, r):
  return (l+r)*(r-l+1)//2
  

N, K = list(map(int, input().split()))
ans = 0
for i in range(K, N+2):
  l = _sum(0, i-1)
  r = _sum(N+1-i,N)
  ans += r-l+1
print(ans%(10**9+7))