n, k = map(int, input().split())
ans = 0
for i in range(1, k + 1):
    if 2 * i % k == 0:
        ans += ((n + k - i) // k) ** 3
print(ans)
