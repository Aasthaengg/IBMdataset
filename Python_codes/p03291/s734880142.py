S=input()
N=len(S)
A=[0]
B=[0]
C=[0]
X=[0]
for i in range(N):
  A.append(A[i])
  B.append(B[i])
  C.append(C[i])
  X.append(X[i])
  if S[i]=='A':
    A[-1]+=1
  elif S[i]=='B':
    B[-1]+=1
  elif S[i]=='C':
    C[-1]+=1
  else:
    X[-1]+=1
P=0
mod=10**9+7
for i in range(N):
  if S[i]=='B':
    P=(P+pow(3,X[N],mod)*A[i]*(C[N]-C[i+1]))%mod
    if X[i]:
      P=(P+pow(3,X[N]-1,mod)*X[i]*(C[N]-C[i+1]))%mod
    if X[N]-X[i+1]:
      P=(P+pow(3,X[N]-1,mod)*A[i]*(X[N]-X[i+1]))%mod
    if X[i] and X[N]-X[i+1]:
      P=(P+pow(3,X[N]-2,mod)*X[i]*(X[N]-X[i+1]))%mod
  if S[i]=='?':
    P=(P+pow(3,X[N]-1,mod)*A[i]*(C[N]-C[i+1]))%mod
    if X[i]:
      P=(P+pow(3,X[N]-2,mod)*X[i]*(C[N]-C[i+1]))%mod
    if X[N]-X[i+1]:
      P=(P+pow(3,X[N]-2,mod)*A[i]*(X[N]-X[i+1]))%mod
    if X[i] and X[N]-X[i+1]:
      P=(P+pow(3,X[N]-3,mod)*X[i]*(X[N]-X[i+1]))%mod
print(P)