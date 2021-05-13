n = int(input())

# 素因数分解
cf = dict()
for nn in range(1, n+1):
    cf.setdefault(2, 0)
    while nn%2 == 0:
        cf[2] += 1
        nn //= 2

    for f in range(3, int(nn**0.5)+ 1, 2):
        cf.setdefault(f, 0)
        while nn%f == 0:
            cf[f] += 1
            nn //= f
    if nn != 1:
        cf.setdefault(nn, 0)
        cf[nn] += 1

ans = 1
mod = 10**9+7
for v in cf.values():
    ans *= (v+1)
    ans %= mod
print(ans)
