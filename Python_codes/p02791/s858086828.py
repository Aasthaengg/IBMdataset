n = int(input())
p = list(map(int, input().split()))
ans = 0
minp = 10**6
for i in range(n):
    minp = min(p[i], minp)
    if minp < p[i]:
        continue
    ans += 1
print(ans)
