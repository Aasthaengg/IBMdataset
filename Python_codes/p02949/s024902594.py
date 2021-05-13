n,m,p=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
distance=[float('inf')]*n
distance[0]=0
for i in range(n-1):
  for j in range(m):
    if distance[l[j][1]-1]>distance[l[j][0]-1]-l[j][2]+p:
      distance[l[j][1]-1]=distance[l[j][0]-1]-l[j][2]+p
x=distance[n-1]
for i in range(n):
  for j in range(m):
    if distance[l[j][1]-1]>distance[l[j][0]-1]-l[j][2]+p:
      distance[l[j][1]-1]=-float('inf')
if distance[n-1]!=x:
  print(-1)
else:
  print(max(-distance[n-1],0))