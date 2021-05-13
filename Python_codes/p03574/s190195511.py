H,W=map(int,input().split())
L=[[] for i in range(H)]
for i in range(H):
  L1=list(input())
  L[i]=L1
L=[["$"]+i+["$"] for i in L]
L=[["$" for i in range(W+2)]]+L+[["$" for i in range(W+2)]]
for i in range(1,H+1):
  for j in range(1,W+1):
    if L[i][j]==".":
      L[i][j]=str([L[i][j+1],L[i-1][j+1],L[i+1][j+1],L[i-1][j-1],L[i+1][j],L[i-1][j],L[i][j-1],L[i+1][j-1]].count("#"))
for i in range(1,H+1):
  print("".join(L[i][1:-1]))