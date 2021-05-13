n, m = map(int, input().split())
mod = 10**9 + 7
# [[素因数,数]]を出力
def fctr1(n):
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f

def comb(n, r):
    res = 1
    for i in range(1, r+1):
        res = res*(n-i+1) % mod
        res = res*pow(i, mod-2, mod) % mod
    return res

prime_count = fctr1(m)
#print(prime_count)
ans = 1
for p, e in prime_count:
    ans *= comb(e+n-1, e)
    ans %= mod
print(ans)