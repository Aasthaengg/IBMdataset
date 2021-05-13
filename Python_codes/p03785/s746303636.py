n, c, k = map(int, input().split())
t_l = []
for _ in range(n):
    t_l.append(int(input()))
t_l.sort()
ans = 0
cnt = 0
for t in t_l:
    if cnt == 0:
        t1 = t
    if t <= t1 + k:
        cnt += 1
        if cnt == c:
            cnt = 0
            ans += 1
    else:
        cnt = 1
        ans += 1
        t1 = t
if cnt != 0:
    ans += 1
print(ans)