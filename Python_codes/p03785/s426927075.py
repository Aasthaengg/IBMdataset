

n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort(reverse=True)

t_b = t[0]
cnt = 0
ans = 0

for i in t:
    # print(i, t_b, cnt, ans)
    if t_b - i <= k and cnt + 1 <= c: # 差がk以下で人数に余裕がある
        cnt += 1
        continue
    else:
        t_b = i
        cnt = 1
        ans += 1

print(ans + 1)