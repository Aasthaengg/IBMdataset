x, y = map(int, input().split())
ans = 10 ** 9 + 3
if y >= x:
    ans = min(ans, abs(y - x))
if - y >= x:
    ans = min(ans, abs(-y - x) + 1)
if y >= -x:
    ans = min(ans, abs(y + x) + 1)
if - y >= -x:
    ans=min(ans, abs(-y + x) + 2)
print(ans)