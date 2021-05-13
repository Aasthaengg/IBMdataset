N,M=map(int,input().split())
stu=[]
for i in range(N):
  a,b=map(int,input().split())
  stu.append([a,b])
pl=[]
for j in range(M):
  c,d=map(int,input().split())
  pl.append([c,d])
for k in range(N):
  met=4*(10**8)+1
  pr=0
  for l in range(M):
    if abs(pl[l][0]-stu[k][0])+abs(pl[l][1]-stu[k][1])<met:
      met=abs(pl[l][0]-stu[k][0])+abs(pl[l][1]-stu[k][1])
      pr=l+1
  print(pr)