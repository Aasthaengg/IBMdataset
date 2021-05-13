from collections import deque
h,w=map(int,input().split())
G=[["#"]*(w+2) for i in range(h+2)]
for i in range(1,h+1):
  G[i]=["#"]+list(input())+["#"]
X=deque()
Y=deque()
V=[[0]*(w+2) for i in range(h+2)]
V[0]=[0]*(w+2)
for i in range(1,h+1):
  V[i]=[0]+[10**7]*w+[0]
V[h+1]=[0]*(w+2)
for i in range(1,h+1):
  for j in range(1,w+1):
    if G[i][j]=="#":
      X.append(i)
      Y.append(j)
      V[i][j]=0
XX=[-1,0,0,1]
YY=[0,-1,1,0]
while len(X)!=0:
  x=X[0]
  y=Y[0]
  X.popleft()
  Y.popleft()
  for i in range(4):
    if V[x+XX[i]][y+YY[i]]==10**7:
      V[x+XX[i]][y+YY[i]]=V[x][y]+1
      X.append(x+XX[i])
      Y.append(y+YY[i])
ans=0
for i in range(h+2):
  for j in range(w+2):
    if V[i][j]>ans:
      ans=V[i][j]
print(ans)