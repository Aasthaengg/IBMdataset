n, m = map(int, input().split())
drink = sorted([list(map(int, input().split())) for _ in range(n)])

ans = 0

for a,b in drink:
    ans += a*min(b,m)
    m -= min(b,m)
    if m == 0:
        break

print(ans)
