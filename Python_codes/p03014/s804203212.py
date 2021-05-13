H,W=map(int,input().split())
G=[ ]

for i in range(H):
  G.append(list(input()))
  
L=[[0]*W for i in range(H)]
R=[[0]*W for i in range(H)]
U=[[0]*W for i in range(H)]
D=[[0]*W for i in range(H)]

for i in range(H):
  for j in range(W):
    k=-i-1
    l=-j-1
    if G[i][j]=="#":
      L[i][j]=0
      U[i][j]=0
    else:
      if j==0:
        L[i][j]=1
        U[i][j]=U[i-1][j]+1
      elif i==0:
        L[i][j]=L[i][j-1]+1
        U[i][j]=1
      else:
        L[i][j]=L[i][j-1]+1
        U[i][j]=U[i-1][j]+1
        
    if G[k][l]=="#":
      R[k][l]=0
      D[k][l]=0
    else:
      if k==-1:
        R[k][l]=1
        D[k][l]=D[k+1][l]+1
      elif i==0:
        R[k][l]=R[k][l+1]+1
        D[k][l]=1
      else:
        R[k][l]=R[k][l+1]+1
        D[k][l]=D[k+1][l]+1
ans=0
for i in range(H):
  for j in range(W):
    #print(L[i][j],R[i][j],U[i][j],D[i][j])
    ans=max(R[i][j]+L[i][j]+U[i][j]+D[i][j]-3,ans)
print(ans)