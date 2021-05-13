n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
all_order=[]
def dfs(a):
  if len(a)==n:
    all_order.append(a)
  else:
    for i in range(n):
      if i in a:continue
      dfs(a+[i])
dfs([])
ans=0
for od in all_order:
  x,y=xy[od[0]]
  for i in od[1:]:
    nx,ny=xy[i]
    ans+=((x-nx)**2+(y-ny)**2)**0.5
    x,y=nx,ny
print(ans/len(all_order))
