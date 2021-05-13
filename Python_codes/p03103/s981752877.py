n, m = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(n)]
d.sort()
ans = 0
for ai, bi in d:
    if m <= bi:
        ans += ai * m
        break
    ans += ai * bi
    m -= bi
print(ans)
