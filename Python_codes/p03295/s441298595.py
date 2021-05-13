n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab.sort(key=lambda x:(x[1], x[0]))

ans = 0
pre_bridge = 0
for i in range(m):
    a, b = ab[i]
    if pre_bridge < a:
        ans += 1
        pre_bridge = b-1
print(ans)