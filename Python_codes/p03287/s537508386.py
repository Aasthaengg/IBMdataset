n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (n + 1)

ans = 0
cnt = {0: 1}
for i in range(n):
    s[i + 1] = s[i] + a[i]
    s[i + 1] %= m
    now = cnt.setdefault(s[i + 1], 0)
    cnt[s[i+1]] = now+1
#print(cnt)

for x in cnt.values():
    ans += x * (x-1) // 2
print(ans)
