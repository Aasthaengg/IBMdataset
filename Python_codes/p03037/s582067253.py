N,M = map(int, input().split())
l=0
r=N
for _ in range(M):
  ll,rr=map(int,input().split())
  l = max(l,ll)
  r = min(r,rr)
ans = r - l + 1
print(ans if ans > 0 else 0)