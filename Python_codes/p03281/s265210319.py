def divisors(n):
    res = 0
    for i in range(1, n+1):
        if n % i == 0:
            res += 1
    return res


N = int(input())
ans = 0

for i in range(1, N+1, 2):
    if divisors(i) == 8:
        ans += 1
print(ans)
