def prime_factorize(n):
    ans = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        c = 0
        while True:
            if not n % i == 0:
                ans.append([i, c])
                break
            n //= i
            c += 1
        if n == 1:
            break
    if n != 1:
        ans.append([int(n), 1])
    return ans

n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
s = [0] * (5 * (10 ** 5))
for i in a:
    p = prime_factorize(i)
    for q in p:
        r = (q[0] - 1) // 2
        s[r] = max(s[r], q[1])
l = 1
for i in range(len(s)):
    l *= pow(max(2 * i + 1, 2), s[i], mod)
    l %= mod
ans = 0
for i in a:
    ans += pow(i, mod - 2, mod) * l % mod
    ans %= mod
print(ans)