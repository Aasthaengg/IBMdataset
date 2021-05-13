import math
N = int(input())
T =  list(int(input()) for n in range(N))
ans = T[0]

for i in range(1,N):
  ans  = ans*T[i] // math.gcd(ans,T[i])
print(ans)