import math
MOD = 10**9+7
n, m = map(int, input().split())

if n == m:
    print( (2 * (math.factorial(n)%MOD)**2) % MOD)
elif abs(n-m) == 1:
    print((max(n, m)*(math.factorial(min(n, m))%MOD)**2) % MOD)
else:
    print(0)
