import sys
input=sys.stdin.readline
def main():
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
  ans=0
  for i in range(R):
    for j in range(C):
      ans=max(ans,dp1[i][j],dp2[i][j],dp3[i][j])
  print(ans)
if __name__ == '__main__':
    main()