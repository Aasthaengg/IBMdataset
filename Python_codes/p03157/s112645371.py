from collections import deque
h,w=map(int,input().split())
G=[["@"]*(w+2) for i in range(h+2)]
for i in range(1,h+1):
  G[i]=["@"]+list(input())+["@"]
V=[[0]*(w+2) for i in range(h+2)]
X=deque([])
Y=deque([])
XX=[-1,0,0,1]
YY=[0,-1,1,0]
ans=0
for i in range(h+2):
  for j in range(w+2):
    if V[i][j]==0 and G[i][j]=="#":
      X.append(i)
      Y.append(j)
      V[i][j]=1
      C=[1,0]
      while len(X)>0:
        x=X[0]
        y=Y[0]
        X.popleft()
        Y.popleft()
        if G[x][y]=="#":
          for k in range(4):
            if V[x+XX[k]][y+YY[k]]==0 and G[x+XX[k]][y+YY[k]]==".":
              X.append(x+XX[k])
              Y.append(y+YY[k])
              V[x+XX[k]][y+YY[k]]=1
              C[1]+=1
        else:
          for k in range(4):
            if V[x+XX[k]][y+YY[k]]==0 and G[x+XX[k]][y+YY[k]]=="#":
              X.append(x+XX[k])
              Y.append(y+YY[k])
              V[x+XX[k]][y+YY[k]]=1
              C[0]+=1
      ans=ans+C[0]*C[1]
print(ans)