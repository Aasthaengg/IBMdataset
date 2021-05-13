# N T
# c1 t1
N, T = map(int, input().split())
c_min = 1001
for _ in range(N):
    c, t = map(int, input().split())
    if c < c_min and t <= T:
        c_min = c
if c_min == 1001:
    print('TLE')
else:
    print(c_min)