n, t_th = map(int, input().split())
c_min = 10000
for i in range(n):
    c, t = map(int, input().split())
    if t <= t_th and c < c_min:
        c_min = c
if c_min == 10000:
    print('TLE')
else:
    print(c_min)
