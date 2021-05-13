n, m, x = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]

INF = 10**9
ans = INF
for i in range(2**n):
    cost = 0
    y = [0]*m
    for j in range(n):
        flg = i & 1
        if flg:
            cost += a[j][0]
            for cm in range(m):
                y[cm] += a[j][cm+1]
        i >>= 1
    for cm in range(m):
        if y[cm] < x:
            break
        if cm == m-1:
            ans = min(ans, cost)
print(ans) if ans < INF else print(-1)