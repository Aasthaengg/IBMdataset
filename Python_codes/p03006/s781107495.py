n=int(input())
xy=[]
for i in range(n):
  x,y=map(int,input().split())
  xy.append((x,y))
pq=[]
for i in range(n):
  for j in range(n):
    if i==j:continue
    x1,y1=xy[i]
    x2,y2=xy[j]
    pq.append((x2-x1,y2-y1))
ans=n
for p,q in pq:
  t=0
  for x,y in xy:
    if (x+p,y+q) not in xy:
      t+=1
  ans=min(ans,t)
print(ans)





