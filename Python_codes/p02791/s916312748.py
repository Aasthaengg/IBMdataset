n = int(input())
p = list(map(int, input().split()))
mi = 10**6
ans = 0
for i in range(n):
    mi = min(mi, p[i])
    if p[i]<=mi:
        ans += 1
print(ans)