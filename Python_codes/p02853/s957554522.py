x, y = map(int, input().split())

ans = 0
p = [300000, 200000, 100000]
if 1 <= x <= 3:
    ans += p[x-1]
if 1 <= y <= 3:
    ans += p[y-1]

if x * y == 1:
    ans += 400000

print(ans)