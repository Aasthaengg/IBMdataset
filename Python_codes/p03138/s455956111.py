N,K=map(int,input().split())
A=list(map(int,input().split()))
X=1<<50
Y,Z=0,0
M=0
for i in range(50):
  X>>=1
  Y,Z=0,0
  for j in range(N):
    if X&A[j]:
      Y+=1
    else:
      Z+=1
  if Y<Z and M+X<=K:
    M+=X
P=0
for i in range(N):
  P+=M^A[i]
print(P)