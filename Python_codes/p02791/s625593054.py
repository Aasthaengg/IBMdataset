n=int(input())
P=list(map(int,input().split()))
ans=1
minp=P[0]
for p in P[1:]:
  minp=min(minp,p)
  if p<=minp:
    ans+=1
print(ans)