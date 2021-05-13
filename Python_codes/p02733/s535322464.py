H,W,K=map(int,input().split())
S=[list(map(int,list(input()))) for i in range(H)]
C=[[0] for i in range(H)]
for i in range(H):
  for j in range(W):
    C[i].append(C[i][j]+S[i][j])
def f(b,l,r):
  R=[0]
  for i in range(H):
    R[-1]+=C[i][r+1]-C[i][l]
    if i!=H-1:
      if b&(1<<i):
        R.append(0)
  return max(R)

INF=10**12
P=INF
Q=0
L=0
for x in range(1<<(H-1)):
  Q=bin(x).count('1')
  L=0
  for i in range(W):
    if f(x,L,i)>K:
      Q+=1
      L=i
      if f(x,L,i)>K:
        Q=INF
        break
  P=min(P,Q)
print(P)