N = int(input())
V = list(map(int,input().split()))

nV = sorted(V)
res = 0
res += (nV[0]+nV[1])/(2**(N-1))

for i in range(2,N):
  res += nV[i]/(2**(N-i))
    
print(res)