x, y = map(int, input().split())
ans = 0
ans += abs(abs(y) - abs(x))
if abs(x) <= abs(y):
    if x < 0:
        ans += 1
    if y < 0:
        ans += 1
else:
    if x >= 0:
        ans += 1
    if y > 0:
        ans += 1
print(ans)
