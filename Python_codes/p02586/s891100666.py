R,C,K=map(int,input().split())
m=[[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
  r,c,v=map(int,input().split())
  m[r][c]=v
d=[[0]*4 for _ in range(R+1)]
for j in range(1,C+1):
  for i in range(1,R+1):
    t=m[i][j]
    if t>0:
      d[i][3]=max(d[i][3],d[i][2]+t)
      d[i][2]=max(d[i][2],d[i][1]+t)
      d[i][1]=max(d[i][1],d[i][0]+t,max(d[i-1])+t)
      d[i][0]=max(d[i][0],max(d[i-1]))
    else:
      d[i][0]=max(d[i][0],max(d[i-1]))
print(max(d[R]))