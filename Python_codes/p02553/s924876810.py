a, b, c, d = map(int, input().split())
ans = -float("inf")
for x in [a, b]:
    for y in [c, d]:
        tmp = x*y
        ans = max(ans, tmp)
print(ans)
