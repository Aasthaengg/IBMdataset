N=int(input())
T=list(map(int,input().split()))
A=list(map(int,input().split()))
X=[T[0]]
Y=[A[-1]]
for i in range(N-1):
  if T[i]<T[i+1]:
    X.append(T[i+1])
  else:
    X.append(0)
  if A[-i-1]<A[-i-2]:
    Y.append(A[-i-2])
  else:
    Y.append(0)
Y=Y[::-1]
for i in range(N):
  if min(X[i],Y[i]) and X[i]!=Y[i]:
    print(0)
    exit()
mod=10**9+7
Z=[max(X[i],Y[i]) for i in range(N)]
C=0
for i in range(N):
  C=max(C,Z[i])
  if C!=T[i]:
    print(0)
    exit()
C=0
for i in range(N):
  C=max(C,Z[-i-1])
  if C!=A[-i-1]:
    print(0)
    exit()
mod=10**9+7
P=1
for i in range(N):
  if Z[i]==0:
    P=P*min(A[i],T[i])%mod
print(P)