def power(x, n, mod):
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * x % mod
        n //= 2
        x = x * x % mod
    return ans

n, k = map(int, input().split())

mod = 10 ** 9 + 7

count = [0] * k
for i in range(k, 0, -1):
    count[i-1] = power(k // i, n, mod)
    j = i * 2
    while j <= k:
        count[i-1] -= count[j-1]
        j += i

ans = 0
for i in range(1, k+1):
    ans = (ans + count[i-1] * i) % mod
print(ans)
