N=int(input())
L=[]
for i in range(1,N):
  if 2**i<=N:
    L.append(2**i)

if N==1:
  print(N)
else:
  print(max(L))