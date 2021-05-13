n,m=map(int,input().split())
war=[list(map(int,input().split())) for i in range(m)]
war=sorted(war)
right=0
left=0
ans=0
for i in range(m):
  if right<=war[i][0]:
    ans+=1
    right=war[i][1]
    left=war[i][0]
  else:
    left=war[i][0]
    right=min(war[i][1],right)
print(ans)