R,C,K=map(int,input().split())
rcv=[list(map(int,input().split())) for _ in range(K)]
mat=[[0]*C for _ in range(R)]
for r,c,v in rcv:
  mat[r-1][c-1]=v
dp=[0]*C
for i in range(R):
  ndp=[0]*C
  wdp=[0]*4
  for j in range(C):
    wdp[0]=max(wdp[0],dp[j])
    if mat[i][j]>0:
      v=mat[i][j]
      wdp[3]=max(wdp[3],wdp[2]+v)
      wdp[2]=max(wdp[2],wdp[1]+v)
      wdp[1]=max(wdp[1],wdp[0]+v)
    ndp[j]=max(wdp)
  dp=ndp.copy()
print(max(wdp))