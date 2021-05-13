# B - Time Limit Exceeded

N, T = map(int, input().split())
INF = 10**18
min_cost = INF
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        min_cost = min(min_cost, c)

if min_cost == INF:
    print('TLE')
else:
    print(min_cost)