n = int(input())
ss = sorted([sorted(input()) for _ in range(n)])
ans = 0
cnt = 1
for i in range(n - 1):
    if ss[i] != ss[i + 1]:
        ans += cnt * (cnt - 1) // 2
        cnt = 0
    cnt += 1
ans += cnt * (cnt - 1) // 2
print(ans)