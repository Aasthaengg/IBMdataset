n, T =  map(int, input().split())

cost = 100000

for i in range(n):
    c, t = map(int, input().split())
    if t <= T:
        cost = min(cost, c)

if cost == 100000:
    print('TLE')
else:
    print(cost)