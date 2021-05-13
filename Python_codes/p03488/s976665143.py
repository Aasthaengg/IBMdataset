s=input()
x,y=map(int,input().split())
ct=0
XY=[]
for i in range(len(s)):
  if s[i]=="F":
    ct+=1
  else:
    XY.append(ct)
    ct=0
XY.append(ct)
x-=XY[0]
X=XY[2::2]
Y=XY[1::2]


def chk(Z,z):
  tot,nz=sum(Z),len(Z)
  if tot==0:
    if z==0:
      return True
    else:
      return False
  elif abs(z)>tot:
    return False
  else:
    DP=[[False]*(2*tot+1) for _ in range(nz+1)]
    DP[0][tot]=True
    for i in range(nz):
      zz=Z[i]
      for j in range(2*tot+1):
        if j+zz<2*tot+1 and DP[i][j+zz]==True:
          DP[i+1][j]=True
        if j-zz>=0 and DP[i][j-zz]==True:
          DP[i+1][j]=True
    return DP[nz][z+tot]

if chk(X,x) and chk(Y,y):
  print("Yes")
else:
  print("No")