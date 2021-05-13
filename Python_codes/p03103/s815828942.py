n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab = sorted(ab, key=lambda x: x[0])
ans = 0
for a, b in ab:
    if m - b > 0:
        ans += a*b
        m -= b
    elif m == b:
        ans += a*b
        m -= b
        break
    else:
        ans += a*m
        break
print(ans)