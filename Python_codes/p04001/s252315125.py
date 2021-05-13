s = input().strip()

cnt = [1]
for i in range(20):
    cnt.append(sum(cnt))
ans = 0
for i in range(len(s)):
    for f in range(i + 1, len(s) + 1):
        num = int(s[i:f])
        ans += num * cnt[i] * cnt[len(s) - f]
print(ans)
