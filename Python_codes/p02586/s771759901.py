import os,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
r,c,k=map(int,input().split())
dp = [0]*(r*c*4)
m=[0]*(r*c)
for i in range(k):
  ri,ci,v=map(int,input().split())
  m[(ri-1)*c+ci-1]=v
dp[0*r*c+0*c+0]=0
dp[1*r*c+0*c+0]=m[0]
dp[2*r*c+0*c+0]=m[0]
dp[3*r*c+0*c+0]=m[0]
for i in range(r):
  for j in range(c):
    if j+1<c:
      dp[0*r*c+i*c+j+1]=max(dp[0*r*c+i*c+j+1],dp[0*r*c+i*c+j])
      dp[1*r*c+i*c+j+1]=max(dp[1*r*c+i*c+j],max(dp[1*r*c+i*c+j+1],dp[0*r*c+i*c+j]+m[i*c+j+1]))
      dp[2*r*c+i*c+j+1]=max(dp[2*r*c+i*c+j],max(dp[2*r*c+i*c+j+1],dp[1*r*c+i*c+j]+m[i*c+j+1]))
      dp[3*r*c+i*c+j+1]=max(dp[3*r*c+i*c+j],max(dp[3*r*c+i*c+j+1],dp[2*r*c+i*c+j]+m[i*c+j+1]))
    if i+1<r:
      a=dp[3*r*c+i*c+j]
      b=a+m[(i+1)*c+j]
      dp[0*r*c+(i+1)*c+j]=a
      dp[1*r*c+(i+1)*c+j]=b
      dp[2*r*c+(i+1)*c+j]=b
      dp[3*r*c+(i+1)*c+j]=b
print(dp[3*r*c+(r-1)*c+c-1])
    
