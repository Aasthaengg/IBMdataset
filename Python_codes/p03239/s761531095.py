N,T=map(int,input().split())
INF=float("inf")
ans=INF
for _ in range(N):
  c,t=map(int,input().split())
  if t<=T:
    ans=min(ans,c)
if ans==INF:
  print("TLE")
else:
  print(ans)