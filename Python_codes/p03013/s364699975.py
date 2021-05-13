MOD=10**9+7
N,M=map(int,input().split())
A=[int(input()) for _ in range(M)]
L=[-1 for _ in range(N)]
p=0
if A == []:
  A=[0]
if 1 == A[p]:
  L[0] = 0
  if p < M-1:
    p +=1
else:
  L[0] = 1
if N>1:
  if 2 == A[p]:
    L[1] = 0
    if p < M-1:
      p+=1
  else:
    L[1]=L[0]+1
for i in range(2,N):
  if i+1 == A[p]:
    L[i] = 0
    if p < M-1:
      p+=1
  else:
    L[i]=L[i-1]+L[i-2]
print(L[-1]%MOD)