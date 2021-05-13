S = int(input())

mod = 10 ** 9 + 7
f = [1]
for i in range(1,2000):
    f.append((f[-1] * i) % mod)
def comb(n,r):
    return f[n] * (pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod) % mod

ans = 0

for i in range(1,700):
    s = S - (3 * i)
    if s < 0:
        break
    ans += comb(s+i-1, i-1)
    ans %= mod

print(ans)