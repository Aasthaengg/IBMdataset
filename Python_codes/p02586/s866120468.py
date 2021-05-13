import sys
input=sys.stdin.readline
r,c,k=map(int,input().split())
l=[0]*((r+1)*(c+1))
for i in range(k):
  a1,a2,a3=map(int,input().split())
  l[a1*(c+1)+a2]=a3
dp0=[[0 for i in range(c+1)] for j in range(r+1)]
dp1=[[0 for i in range(c+1)] for j in range(r+1)]
dp2=[[0 for i in range(c+1)] for j in range(r+1)]
dp3=[[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
  for j in range(c):
    x=l[i*(c+1)+j+1]
    y=l[(i+1)*(c+1)+j]
    dp3[i+1][j+1]=max(dp2[i][j+1]+x,dp3[i][j+1],dp2[i+1][j]+y,dp3[i+1][j])
    dp2[i+1][j+1]=max(dp2[i][j+1]+x,dp3[i][j+1],dp1[i+1][j]+y,dp2[i+1][j])
    dp1[i+1][j+1]=max(dp2[i][j+1]+x,dp3[i][j+1],dp0[i+1][j]+y,dp1[i+1][j])
    dp0[i+1][j+1]=max(dp2[i][j+1]+x,dp3[i][j+1],dp0[i+1][j])
z=l[r*(c+1)+c]
print(max(dp2[r][c]+z,dp3[r][c]))