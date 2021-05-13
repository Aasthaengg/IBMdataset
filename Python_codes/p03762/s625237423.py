n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10**9 + 7

r = [0] # r[i] : xiと、xiより左の縦の直線を使用した長方形の横の辺の長さの総和
for i in range(1, n):
    r.append(r[-1] + (x[i] - x[i-1]) * i)

dp_h = [0] * n # dp[i] : 左からi本目までの縦の直線のうち2本を使用したときの長方形の横の辺の長さの総和
for i in range(1, n):
    dp_h[i] = (dp_h[i-1] + r[i]) % MOD

u = [0]
for i in range(1, m):
    u.append(u[-1] + (y[i] - y[i-1]) * i)

dp_v = [0] * m
for i in range(1, m):
    dp_v[i] = (dp_v[i-1] + u[i]) % MOD

print((dp_h[n-1] * dp_v[m-1]) % MOD)