p = 998244353
N = 2*10**5
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % p

def main():
    n, m, k = [int(i) for i in input().split()]
    res = 0
    for tk in range(0, k+1):
        res = (res + m * cmb(n-1, tk, p) * pow(m-1, n-tk-1, p)) % p
    print(res)

if __name__ == '__main__':
    main()

