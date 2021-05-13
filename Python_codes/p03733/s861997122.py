N, T = map(int, input().split())
ts = list(map(int, input().split()))

ans = T
current = T
for t in ts[1:]:
    if t < current:
        ans += T + t - current
        current = t + T
    else:
        ans += T
        current = t + T
print(ans)
