N, T = map(int, input().split())
INF = 10**9
res = INF
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T and c < res:
        res = c
print(res if res != INF else 'TLE')
