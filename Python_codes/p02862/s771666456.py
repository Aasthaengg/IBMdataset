mod = 10**9+7
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]


def init(n):
    for i in range(2, n + 1):
        fac.append(fac[-1] * i % mod)
        inv.append(-inv[mod % i] * (mod // i) % mod)
        finv.append(finv[-1] * inv[-1] % mod)


def com(n, k, mod):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


X, Y = map(int, input().split())
b = max([X, Y])
s = min([X, Y])
if s - (b-s) < 0 or not (s-(b-s)) % 3 == 0:
    print(0)
    exit()

s_t = (s-(b-s))//3
b_t = (s-(b-s))//3 + (b-s)
a = s_t + b_t
b = b_t
p = 10**9 + 7
init(a)
print(com(a, b, p))
