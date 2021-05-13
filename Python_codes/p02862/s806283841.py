from functools import reduce

def combination2(n, r, MOD=10**9+7):
    if not 0 <= r <= n: return 0
    r = min(r, n - r)
    numerator = reduce(lambda x, y: x * y % MOD, range(n, n - r, -1), 1)
    denominator = reduce(lambda x, y: x * y % MOD, range(1, r + 1), 1)
    return numerator * pow(denominator, MOD - 2, MOD) % MOD

X, Y = map(int, input().split())
if (2*X-Y)%3 or (2*Y-X)%3:
    print(0)
    exit()
x, y = (2*X-Y)//3, (2*Y-X)//3
print(combination2(x+y,x))
