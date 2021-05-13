N,W=map(int,input().split())

wvlist=[]
for i in range(N):
  w,v=map(int,input().split())
  wvlist.append((w,v))
  
#normalize
w1=wvlist[0][0]

w2vlist=[]
for i in range(N):
  w,v=wvlist[i]
  w2vlist.append((w,w-w1,v))
#print(w2vlist)

dp=[[[0]*(3*N+1) for _ in range(N+1)] for _ in range(N+1)]
#print(dp)

for i in range(1,N+1):
  w,wd,v=w2vlist[i-1]
  for j in range(1,i+1):
    for k in range(3*N+1):
      dp[i][j][k]=dp[i-1][j][k]
      if k-wd>=0:
        dp[i][j][k]=max(dp[i][j][k],dp[i-1][j-1][k-wd]+v)

max_answer=0
for j in range(N+1):
  for k in range(3*N+1):
    if w1*j+k<=W:
      max_answer=max(max_answer,dp[N][j][k])
      #print(j,k,dp[N][j][k])
      
print(max_answer)