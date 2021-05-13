N, M = map(int, input().split())
dic = {}
if N == 1:
    print(1)
    exit()
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        if 2 not in dic:
            dic[2] = 1
        else:
            dic[2] += 1
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f not in dic:
                dic[f] = 1
            else:
                dic[f] += 1
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
        a.append(n)
    return a

n = 10 ** 9
k = 2 * 10 ** 5
mod = 10**9 + 7

modinv_table = [-1] * (k+1)
modinv_table[1] = 1
for i in range(2, k+1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans

prime_factorize(M)
res = 1
for k, v in dic.items():
    if v == 1:
        res *= N % mod
    else:
        res *= binomial_coefficients((v + N - 1), (N - 1)) % mod
print(res % mod)
