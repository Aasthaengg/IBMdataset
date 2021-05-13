N, M = map(int, input().split())
mod = 10 ** 9 + 7
m = 0


def factorization(n):
    if n == 1:
        return []
    arr = []
    temp = n
    global m
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append((i, cnt))
            m = max(m, cnt)

    if temp!=1:
        arr.append((temp, 1))

    if arr==[]:
        arr.append((n, 1))

    return arr


fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]


def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


for i in range(2, 2 * N + 2 * m + 10):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


A = factorization(M)
ans = 1

for (key, value) in A:
    ans *= cmb(value + N - 1, value)
    ans %= mod

print(ans)