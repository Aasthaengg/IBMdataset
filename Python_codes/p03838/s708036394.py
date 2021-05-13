x, y = map(int, input().split())

ans = 2* (10 **9)

if y - (-x) >= 0:
    ans = y + x + 1

if -y -x >= 0:
    ans = min(ans, -y -x + 1)

if -y - (-x) >= 0:
    ans = min(ans, -y +x +2)

if y - x >= 0:
    ans = min(ans, y-x)

print(ans)