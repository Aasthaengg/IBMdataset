R,C,K=map(int,input().split())
value=[[0]*(C+1) for i in range(R+1)]
for i in range(K):
  r,c,v=map(int,input().split())
  value[r][c]=v
DP0=[[0]*(C+1) for i in range(R+1)]
DP1=[[0]*(C+1) for i in range(R+1)]
DP2=[[0]*(C+1) for i in range(R+1)]
DP3=[[0]*(C+1) for i in range(R+1)]
for i in range(1,R+1):
  for j in range(1,C+1):
    v=value[i][j]
    a=DP0[i][j-1]
    b=DP1[i][j-1]
    c=DP1[i-1][j]
    d=DP2[i-1][j]
    e=DP3[i-1][j]
    f=DP2[i][j-1]
    DP0[i][j]=max(a,c,d,e)
    DP1[i][j]=max(DP0[i-1][j]+v,c+v,d+v,e+v,b,a+v)
    DP2[i][j]=max(b+v,f)
    DP3[i][j]=max(f+v,DP3[i][j-1])

print(max(DP0[R][C],DP1[R][C],DP2[R][C],DP3[R][C]))