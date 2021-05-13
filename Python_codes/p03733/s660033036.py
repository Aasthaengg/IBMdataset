n, t = map(int, input().split())
time = list(map(int, input().split()))

diff = [t1 - t0 for t0, t1 in zip(time, time[1:])]

ans = 0
for dt in diff:
    if dt <= t:
        ans += dt
    else:
        ans += t

print(ans + t)
