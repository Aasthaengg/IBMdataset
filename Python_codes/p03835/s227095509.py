from collections import defaultdict

k, s = map(int, input().split())

cnt = defaultdict(int)
for x in range(k+1):
    for y in range(k+1):
        cnt[x+y] += 1

ans = 0
for key, value in cnt.items():
    if 0 <= s - key <= k:
        ans += value

print(ans)
