N = int(input())
As = list(map(int, input().split()))

Bs = [0]*N

Bs[0] = sum(As[::2]) - sum(As[1::2])

for i in range(1,N):
  Bs[i] = 2*As[i-1] - Bs[i-1]
  
Bs = map(str, Bs)
print(" ".join(Bs))