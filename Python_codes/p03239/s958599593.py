N,T=map(int,input().split())
c=[list(map(int,input().split())) for i in range(N)]
ans=10**4
for i in range(N):
  if c[i][1]<=T:
    ans=min(ans,c[i][0])
if ans==10**4:
  ans='TLE'
print(ans)