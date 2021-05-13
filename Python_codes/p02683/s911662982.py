n, m, x = map(int, input().split())

c = [0] * n
a = [[] for _ in range(n)]

for i in range(n):
    ca = list(map(int, input().split()))
    c[i], a[i] = ca[0], ca[1:]

ans = INF = 1e+9

for s in range(1 << n):
    skill = [0] * m
    money = 0
    for i in range(n):
        # don't buy a book
        if (s >> i) % 2 == 0:
            continue
        money += c[i]
        for j in range(m):
            skill[j] += a[i][j]
    flag = 1
    for k in range(m):
        if skill[k] < x:
            flag = 0
    if flag:
        ans = min(ans, money)
if ans == INF:
    ans = -1

print(ans)