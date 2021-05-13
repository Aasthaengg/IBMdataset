N,A,B=map(int,input().split())
V=sorted(list(map(int,input().split())),reverse=True)
D=dict()
for i in range(N):
  D[V[i]]=D.get(V[i],0)+1
X=[1]
for i in range(1,51):
  X.append(X[-1]*i)
def cmb(n,r):
  return X[n]//(X[r]*X[n-r])

P=0
if V[0]==V[A-1]:
  for i in range(A,B+1):
    if i>D[V[0]]:
      break
    P+=cmb(D[V[0]],i)
else:
  Q=0
  for i in range(A-1,-1,-1):
    if V[i]!=V[A-1]:
      break
    Q+=1
  P=cmb(D[V[A-1]],Q)
print(sum(V[:A])/A)
print(P)