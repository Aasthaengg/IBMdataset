x, y = map(int, input().split())

ans = 10**18

if y - x >= 0:
    ans = min(ans, y-x)

x *= -1

if y - x >= 0:
    ans = min(ans, y-x+1)

x *= -1
y *= -1

if y - x >= 0:
    ans = min(ans, y-x+1)

x *= -1

if y - x >= 0:
    ans = min(ans, y-x+2)

print(ans)