N,T = map(int,(list(input().split())))
cost = 1001
for _ in range(N):
    c,t = map(int,(list(input().split())))
    if t<=T:
        cost=min(cost,c)
if cost == 1001:
    print('TLE')
else:
    print(cost)

