N=int(input())
L=list()
L.append(2)
L.append(1)
for i in range(2,N+1):
  L.append(L[i-2]+L[i-1])
print(L[N])