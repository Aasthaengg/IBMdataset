S = int(input())

res = 0
cnt = 1
mod = 10 ** 9 + 7
def f(n, r):
    X = 1
    Y = 1
    for i in range(r):
        X *= n - i    # nCr の分子
        X %= mod
        Y *= i + 1    # nCr の分母
        Y %= mod

    # フェルマーの小定理より (X/Y)%mod = X*Y^(mod - 2) % mod
    return X * pow(Y, mod - 2, mod) % mod

while S >= cnt * 3:
    tmp = S - (cnt * 3)
    res += f(tmp + cnt - 1, tmp)
    res %= mod
    cnt += 1

print(res)