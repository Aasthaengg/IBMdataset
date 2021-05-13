N=int(input())
A=list(map(int,input().split()))
if N==0:
  if A[0]==1:
    print(1)
  else:
    print(-1)
  exit()
if A[0]:
  print(-1)
  exit()
C=[A[N]]
for i in range(N):
  C.append(C[i]+A[-i-2])
C=C[::-1]
B=[1]
P=1
for i in range(N):
  if (B[i]<<1)<A[i+1]:
    print(-1)
    exit()
  P+=min((B[i]<<1),C[i+1])
  B.append(min((B[i]<<1),C[i+1])-A[i+1])
  if B[-1]<0:
    print(-1)
    exit()
print(P)