n, t = map(int, input().split())
times = list(map(int, input().split()))

p = 0
ans = 0
for time in times:
    start = min(p, time)
    ans += t - max(0, p - time)
    p = time + t
print(ans)
