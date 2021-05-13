n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    minp = min(p[i], p[i + 1], p[i + 2])
    maxp = max(p[i], p[i + 1], p[i + 2])
    if p[i + 1] != minp and p[i + 1] != maxp:
        ans += 1
print(ans)
