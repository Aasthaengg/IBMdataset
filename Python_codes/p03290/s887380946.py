d,g = map(int, input().split())
ps = []
cs = []
for i in range(d):
    p,c = map(int, input().split())
    ps.append(p)
    cs.append(c)
INF = 1 << 50
dp = [INF]*110000
dp[0] = 0
for k,(p,c) in enumerate(zip(ps,cs)):
    tmp = dp[:]
    for i in range(p+1):
        for j in range(g//100+1):
            if dp[j] == INF:continue
            if i < p:
                tmp[j+(k+1)*i] = min(dp[j+(k+1)*i], dp[j]+i)
            else:
                tmp[j+(k+1)*i+c//100] = min(dp[j+(k+1)*i+c//100], dp[j]+i)
    dp = tmp[:]
print(min(dp[g//100:]))