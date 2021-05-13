N,M=map(int,input().split())
L=list()
for i in range(M):
  a,b=map(int,input().split())
  A=list([b,a])
  L.append(A)
L=sorted(L)
R=[L[0][0]-1]
for j in range(M):
  if R[-1] not in range(L[j][1],L[j][0]):
    R.append(L[j][0]-1)
print(len(R))