N = int(input())
T,A = list(map(int,input().split()))
H = list(map(int,input().split()))
MinDif = 1000
for i in range(N):
  Temp = T - H[i] * 0.006
  if abs(Temp - A) == min( MinDif, abs(Temp - A) ):
    MinDif = abs(Temp - A)
    ans = i + 1
print(ans)