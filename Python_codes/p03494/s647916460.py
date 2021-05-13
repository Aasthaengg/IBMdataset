import math
N = int(input())
A = list(map(int,input().split()))

g = A[0]
for i in range(N):
  g = math.gcd(g,A[i])

cnt = 0
while g % 2 == 0:
  g = g//2
  cnt += 1

print(cnt)