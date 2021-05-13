mod = 1000000007

def pow_mod(x, y):
    res = 1
    while y > 0:
        if y % 2:
            res *= x
            res %= mod
        x *= x
        x %= mod
        y //= 2
    return res

def divs(x):
    res = []
    for i in range(1, x+1):
        if i * i > x:
            break
        if x % i != 0:
            continue
        res.append(i)
        if i != x // i:
            res.append(x // i)
    return res

N, K = list(map(int, input().split()))

num = [0] * 100010
for g in range(1, K+1):
    num[g] = pow_mod(K // g, N)


for x in range(K, 0, -1):
    div = divs(x)
    for i in div:
        if i == x:
            continue
        num[i] += mod - num[x]
        num[i] %= mod

ans = 0
for g in range(1, K+1):
    ans += g * num[g] % mod
    ans %= mod
print(ans)
