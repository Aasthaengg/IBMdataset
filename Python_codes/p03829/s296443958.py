n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for e1, e2 in zip(x, x[1:]):
    walk = (e2 - e1) * a
    ans += min(walk, b)

print(ans)
