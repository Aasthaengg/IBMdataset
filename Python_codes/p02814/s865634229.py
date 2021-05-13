import math
N,M = map(int,input().split())
A = list(map(int,input().split()))
LCM = A[0]
for i in range(1, N):
    LCM = LCM * A[i] // math.gcd(LCM, A[i])
 
for i in range(N):
  temp = LCM//A[i]
  if temp%2 == 0: #存在しない
    print(0)
    exit()
MIN = LCM//2
nokori = M - MIN
#print(MIN,nokori,LCM)
ans = nokori//LCM + 1
print(ans)