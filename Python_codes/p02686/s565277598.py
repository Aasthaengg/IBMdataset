N=int(input())
S=[input() for i in range(N)]
a,b=0,0
X=[]
Y=[]
for i in range(N):
  a,b=0,0
  for j in range(len(S[i])):
    if S[i][j]=='(':
      a+=1
    else:
      a-=1
    b=min(b,a)
  b=-b
  a=a+b
  if a>b:
    X.append((b,a))
  else:
    Y.append((b,a))
P=0
Q=0
X.sort()
for i in range(len(X)):
  P=max(P,Q+X[i][0])
  Q=Q+X[i][0]-X[i][1]
Y.sort(key=lambda x:-x[1])
for i in range(len(Y)):
  P=max(P,Q+Y[i][0])
  Q=Q+Y[i][0]-Y[i][1]
if P or Q:
  print('No')
else:
  print('Yes')