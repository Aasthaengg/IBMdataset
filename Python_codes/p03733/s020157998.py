N, T = map(int, input().split())
ans = 0
t_start = 0
t_stop = 0
for t in map(int, input().split()):
    if t >= t_stop:
        ans += t_stop - t_start
        t_start = t
    t_stop = t + T
print(ans + t_stop - t_start)
