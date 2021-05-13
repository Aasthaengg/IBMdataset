N, K = map(int, input().split())
cnt = [0 for _ in range(10**5 + 10)]

for i in range(N):
    a, b = map(int, input().split())
    cnt[a] += b

res = 0
for i in range(len(cnt)):
    res += cnt[i]
    if res >= K:
        break
print(i)