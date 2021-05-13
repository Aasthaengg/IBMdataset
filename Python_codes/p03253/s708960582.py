def prime_factorize(n):
    ans = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        while True:
            if not n % i == 0:
                break
            ans.append(i)
            n /= i
        if n == 1:
            break
    if n != 1:
        ans.append(int(n))
    return ans

def comb(n, r, p):
    x, y = 1, 1
    for i in range(n, n - r, -1):
        x *= i
        y *= i + r - n
        x %= p
        y %= p
    return pow(y, p - 2, p) * x % p

n, m = map(int, input().split())
mod = 10 ** 9 + 7
s = prime_factorize(m)
if m == 1:
    s = [1]
c = 0
d = s[0]
ans = 1
for i in range(len(s)):
    if d == s[i]:
        c += 1
    else:
        d = s[i]
        ans *= comb(n - 1 + c, c, mod)
        ans %= mod
        c = 1
ans *= comb(n - 1 + c, c, mod)
ans %= mod
if m == 1:
    ans = 1
print(ans)