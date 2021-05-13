n, k = map(int, input().split())

cnt = [0] * (n + 1)

for i in range(1, n + 1):
    cnt[i % k] += 1

if k % 2 == 0:
    ans = 0
    ans += cnt[0] * cnt[0] * cnt[0]
    if k // 2 <= n:
        ans += cnt[k // 2] * cnt[k // 2] * cnt[k // 2]
    print(ans)
else:
    print(cnt[0] * cnt[0] * cnt[0])

