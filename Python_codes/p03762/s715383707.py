N,M = map(int, input().split())
X = [int(i) for i in input().split()]
Y = [int(i) for i in input().split()]

MOD = 10 ** 9 + 7

def f(Z:list):
    res = 0
    for k, z in enumerate(Z, 1):
        res = (res + (k - 1) * z - (len(Z) - k) * z) % MOD
    return res

print(f(X) * f(Y) % MOD)