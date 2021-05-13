N, T = map(int, input().split())
cost = []

for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        cost.append(c)
    
print('TLE' if len(cost) == 0 else min(cost))