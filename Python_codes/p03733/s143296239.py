n, t = map(int, input().split())
data = list(map(int, input().split()))

ans = t + 0
cum_time = 0
for d in data:
    dt = d - cum_time
    if dt < t:
        lost = t - dt
        ans -= lost
    ans += t
    cum_time += dt

print(ans)