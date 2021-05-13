MOD = 10 ** 9 + 7

n, k = map(int, input().split())

ans = 0
for i in range(k, n + 2):
    cnt = i * (n + n - i + 2) // 2 - i * i // 2 + 1
    ans += cnt
    ans %= MOD
print(ans)