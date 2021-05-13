L=list()
R=list()
T=0
N,M=map(int,input().split())
for i in range(N):
  A,B=map(int,input().split())
  L.append(A)
  R.append(B)
c = zip(L, R)
c=sorted(c)
L, R = zip(*c)
L=list(reversed(L))
R=list(reversed(R))
while True:
  c=L[-1]
  T+=c*min(M,R[-1])
  M-=min(M,R[-1])
  L.pop(-1)
  R.pop(-1)
  if M==0:
    break
print(T)