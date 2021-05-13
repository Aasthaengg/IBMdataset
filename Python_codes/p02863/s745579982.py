n, t = map(int, input().split())
a = [0]
b = [0]
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

dp1 = [[0] * t for _ in range(n+2)]
dp2 = [[0] * t for _ in range(n+2)]

for i in range(n):
    for j in range(t):
        if a[i+1] > j:
            dp1[i+1][j] = dp1[i][j]
        else:
            dp1[i+1][j] = max(dp1[i][j], dp1[i][j-a[i+1]] + b[i+1])

for i in range(n+1, 1, -1):
    for j in range(t):
        if a[i-1] > j:
            dp2[i-1][j] = dp2[i][j]
        else:
            dp2[i-1][j] = max(dp2[i][j], dp2[i][j-a[i-1]] + b[i-1])

ans = 0
for i in range(1, n+1):
    for j in range(t):
        total = b[i] +dp1[i-1][j] + dp2[i+1][t-1-j]
        ans = max(ans, total)
print(ans)