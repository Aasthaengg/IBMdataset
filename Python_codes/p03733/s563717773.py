N, T = map(int, input().split())
times = list(map(int, input().split()))
ans = 0
t = 0
for time in times:
    if time >= t:
        ans += T
        t = time + T
    else:
        diff = t - time
        ans += T - diff
        t = time + T
print(ans)