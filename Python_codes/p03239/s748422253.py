n, T = map(int, input().split())
d = list(c for c, t in (map(int, input().split()) for _ in range(n)) if t <= T)
if d:
    print(min(d))
else:
    print('TLE')
