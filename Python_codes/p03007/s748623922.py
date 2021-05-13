N=int(input())
A=list(map(int,input().split()))
A.sort()
P=0
Q=[]
if A[0]<=0 and A[-1]>=0:
  B,C=[],[]
  for i in range(N):
    if A[i]==0:
      if len(B)==0:
        B.append(0)
      else:
        C.append(0)
    else:
      if A[i]<0:
        B.append(A[i])
      else:
        C.append(A[i])
  for i in range(len(C)-1):
    Q.append([B[0],C[-1]])
    B[0]-=C[-1]
    del C[-1]
  for i in range(len(B)):
    Q.append([C[0],B[-1]])
    C[0]-=B[-1]
    del B[-1]
  P=C[0]
else:
  if A[0]>0:
    for i in range(N-2,0,-1):
      Q.append([A[0],A[i]])
      A[0]-=A[i]
    Q.append([A[-1],A[0]])
    P=A[-1]-A[0]
  else:
    for i in range(N-1):
      Q.append([A[-1],A[i]])
      A[-1]-=A[i]
    P=A[-1]
print(P)
for i in range(N-1):
  print(*Q[i])