N, T = map(int, input().split())
c, t = [], []
min_cost = 1001

for _ in range(N):
    c_, t_ = map(int, input().split())
    c.append(c_)
    t.append(t_)

for i in range(N):
    if t[i] <= T:
        if c[i] < min_cost:
            min_cost = c[i]
            
if min_cost != 1001:
    print(min_cost)
else:
    print('TLE')