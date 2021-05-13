[n,m] = [int(i) for i in input().split()]
ls = [1]
mod = 10 ** 9 + 7
for i in range(1,10**5+1):
    ls.append((ls[-1]*i) % mod)

if abs(n-m) >= 2:
    print(0)
else:
    ans = (ls[n] * ls[m]) % mod
    if n == m:
        ans *= 2
        ans %= mod
    print(ans)
