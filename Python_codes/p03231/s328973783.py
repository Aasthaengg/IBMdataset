import math

N, M = map(int, input().split())
S = input()
T = input()

GCD = math.gcd(N, M)
a, b = N//GCD, M//GCD
ans = True
for i in range(GCD):
    if S[i*a] != T[i*b]:
        ans = False
        break

if ans:
    print(a*b*GCD)
else:
    print(-1)