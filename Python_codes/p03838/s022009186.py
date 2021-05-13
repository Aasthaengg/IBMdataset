x, y = map(int, input().split())

ans = 1 << 35
 
# x to y
if x <= y: ans = min(ans, y - x)
# -x to y
if -x <= y: ans = min(ans, 1 + y - (-x))
# x to -y
if x <= -y: ans = min(ans, -y - x + 1)
# -x to -y
if -x <= -y: ans = min(ans, 1 + -y - (-x) + 1)

print(ans)

