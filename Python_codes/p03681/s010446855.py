import math
N,M = map(int,input().split())
f = 1
if abs(N-M) > 1:
    print(0)
    exit()
if (N+M) % 2 == 0:
    f = 2

print(math.factorial(N) * math.factorial(M) * f % (10**9+7))