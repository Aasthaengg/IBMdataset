n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
distance=[9999999999999999]*n
distance[0]=0
for i in range(n-1):
  for j in range(m):
    if distance[l[j][1]-1]>distance[l[j][0]-1]-l[j][2]:
      distance[l[j][1]-1]=distance[l[j][0]-1]-l[j][2]
f=[0]*n
for i in range(n):
  for j in range(m):
    if distance[l[j][1]-1]>distance[l[j][0]-1]-l[j][2]:
      distance[l[j][1]-1]=distance[l[j][0]-1]-l[j][2]
      f[l[j][1]-1]=1
    if f[l[j][0]-1]==1:
      f[l[j][1]-1]=1
if f[n-1]==0:
  print(-distance[n-1])
else:
  print('inf')