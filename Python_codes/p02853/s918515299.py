x, y = map(int, input().split())
p = [0, 300000, 200000, 100000]
ans = 0
if x == 1 and y == 1:
    ans += 400000

for a in [x, y]:
    if a <= 3:
        ans += p[a]
print(ans)