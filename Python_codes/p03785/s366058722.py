n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()

t_crr = t[0]
cnt = 0
ans = 1

for i in t:
    # print(cnt, ans, t_crr, i)
    if i - t_crr <= k and cnt < c:
        cnt += 1
        continue
    else:
        t_crr = i
        ans += 1
        cnt = 1

print(ans)