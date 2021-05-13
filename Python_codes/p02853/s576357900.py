x, y = map(int, input().split())
ans = 0
for p in [x, y]:
    ans += max(0, 4-p) * 100000
if x == 1 and y == 1:
    ans += 400000
print(ans)