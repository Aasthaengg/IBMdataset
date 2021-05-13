n, t = map(int, input().split())

INF = 2000
cost = INF 
for i in range(n):
    c, time = map(int, input().split())
    if t >= time:
        cost = min(cost, c)

if cost == INF:
    print('TLE')
else:
    print(cost)