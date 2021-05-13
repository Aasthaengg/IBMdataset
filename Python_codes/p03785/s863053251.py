n, c, k = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

ans = 0
cnt = 0
tmp_t = 0
for t in arr:
    if cnt == 0:
        tmp_t = t
    cnt += 1
    if t - tmp_t > k:
        ans += 1
        cnt = 1
        tmp_t = t
    elif cnt == c:
        ans += 1
        cnt = 0
if cnt:
    ans += 1

print(ans)
