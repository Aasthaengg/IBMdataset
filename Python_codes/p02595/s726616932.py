n,d=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n):
  if l[i][0]**2+l[i][1]**2<=d**2:
    ans+=1
print(ans)