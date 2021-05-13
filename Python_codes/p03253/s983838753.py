n, m = map(int, input().split())
mod = 10 ** 9 + 7
if m == 1:
    print(1)
    exit()

f = [1 for _ in range(10 ** 7)]
f_inv = [1 for _ in range(10 ** 7)]
for i in range(1, 10 ** 6):
    f[i] = f[i-1] * i % mod
    f_inv[i] = pow(f[i], mod-2, mod)

def comb(n, k):
    return f[n] * f_inv[k] * f_inv[n-k] % mod
def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(n**0.5)+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])

    if tmp != 1:
        arr.append([tmp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

arr = factorization(m)

ans = 1
for _, k in arr:
    ans *= comb(n+k-1, k)
    ans %= mod

print(ans)