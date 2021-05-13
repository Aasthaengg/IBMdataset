R,C,K=map(int, input().split())
M=[[0 for i in range(C)]for i in range(R)]
for i in range(K):
  r,c,v=map(int, input().split())
  r-=1
  c-=1
  M[r][c]=v
dp0=[[0 for j in range(C)] for i in range(R)]
dp1=[[0 for j in range(C)] for i in range(R)]
dp2=[[0 for j in range(C)] for i in range(R)]
dp3=[[0 for j in range(C)] for i in range(R)]
dp1[0][0]+=M[0][0]
for r in range(R):
  for c in range(C):
    if 0<r:
      dp1[r][c]=max(max(dp1[r-1][c],dp2[r-1][c],dp3[r-1][c])+M[r][c],dp1[r][c])
      dp0[r][c]=max(max(dp1[r-1][c],dp2[r-1][c],dp3[r-1][c]),dp0[r][c])
    if 0<c:
      dp3[r][c]=max(dp2[r][c-1]+M[r][c],dp3[r][c],dp3[r][c-1])
      dp2[r][c]=max(dp1[r][c-1]+M[r][c],dp2[r][c],dp2[r][c-1])
      dp1[r][c]=max(dp0[r][c-1]+M[r][c],dp1[r][c],dp1[r][c-1])
      dp0[r][c]=max(dp0[r][c-1],dp0[r][c])
print(max(dp1[-1][-1],dp2[-1][-1],dp3[-1][-1]))