H,W,D=map(int,input().split())
G=[[]]*(H*W)
J=[0]*(H*W)
for i in range(H):
  for j,a in enumerate(list(map(int,input().split()))):
    G[a-1]=[i,j]
    
for i in range(H*W):
  if i-D>=0:
    J[i]=J[i-D]+abs(G[i][0]-G[i-D][0])+abs(G[i][1]-G[i-D][1])
      
for i in range(int(input())):
  l,r=map(int,input().split())
  print(J[r-1]-J[l-1])