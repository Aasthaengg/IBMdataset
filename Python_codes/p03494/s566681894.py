from math import gcd
N = int(input())
A = list(map(int, input().split()))
g = A[0]
for i in range(1, N):
  g = gcd(g, A[i])
ans = 0
while g % 2 == 0:
  g //= 2
  ans += 1
print(ans)