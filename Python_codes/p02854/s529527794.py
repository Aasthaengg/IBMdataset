N ,*A  = map(int,open(0).read().split())

L = [0 for i in range(N+1)]
D = [0 for i in range(N)]

for i,a in enumerate(A,1):
  L[i] = L[i-1] + a
for i in range(N):
  D[i] = L[-1]-L[i]
#L.pop(0)
  
#print(L)
#print(D)
ans = 1e19
for i in range(N):
  #print(L[i],D[i],L[i]-D[i])
  ans = min(abs(L[i]-D[i]),ans)
print(ans)