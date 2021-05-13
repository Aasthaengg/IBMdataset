def enumDivisor(n):
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if i * i != n:
                ans.append(n // i)
    return ans


n = int(input())

ans = 0

for k in enumDivisor(n):
    if k == 1:
        continue
    tmp = n
    while tmp % k == 0:
        tmp //= k
    tmp %= k
    if tmp == 1:
        ans += 1

ans += len(enumDivisor(n - 1)) - 1

print(ans)
