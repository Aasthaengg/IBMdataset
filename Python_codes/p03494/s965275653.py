N = int(input())
A = list(map(int,input().split()))

import math
x = A[0]
for i in range(1,N):
    x = math.gcd(x,A[i])

ans = 0
while x%2 == 0:
    x = x//2
    ans += 1

print(ans)
