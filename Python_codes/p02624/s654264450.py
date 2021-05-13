n = int(input())
ans = 0
for i in range(1, int(n ** 0.5) + 1):
    k = n // i
    ans += i * k * (k + 1) // 2
    if i != k:
        l = n // (i + 1)
        ans += i * (i + 1) * (k + l + 1) * (k - l) // 4
print(ans)