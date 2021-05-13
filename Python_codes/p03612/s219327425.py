n = int(input())
p = list(map(int, input().split())) + ['*']

ans = 0
for i, v in enumerate(p, 1):
    if i == v:
        p[i-1], p[i] = p[i], p[i-1]
        ans += 1

print(ans)
