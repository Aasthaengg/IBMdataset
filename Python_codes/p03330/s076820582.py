n,c=map(int,input().split())
d=[list(map(int,input().split())) for i in range(c)]
g=[list(map(int,input().split())) for i in range(n)]
mod0=set()
mod1=set()
mod2=set()
for i in range(n):
  for j in range(n):
    if (i+j+2)%3==0:
      mod0.add((i,j))
    elif (i+j+2)%3==1:
      mod1.add((i,j))
    else:
      mod2.add((i,j))
cost1=[0]*c
for c1 in range(c):
  tmp=0
  for y,x in mod0:
    tmp+=d[g[y][x]-1][c1]
  cost1[c1]+=tmp
cost2=[0]*c
for c2 in range(c):
  tmp=0
  for y,x in mod1:
    tmp+=d[g[y][x]-1][c2]
  cost2[c2]+=tmp
cost3=[0]*c
for c3 in range(c):
  tmp=0
  for y,x in mod2:
    tmp+=d[g[y][x]-1][c3]
  cost3[c3]+=tmp
ans=10**18
for c1 in range(c):
  for c2 in range(c):
    for c3 in range(c):
      if c1==c2 or c2==c3 or c3==c1:
        continue
      ans=min(ans,cost1[c1]+cost2[c2]+cost3[c3])
print(ans)