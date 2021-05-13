n, x = map(int, input().split())
ans = 0
mi = 1000
total = 0
for i in range(n):
    m = int(input())
    mi = min(mi, m)
    total += m
    ans += 1
ans += (x - total) // mi
print(ans)
