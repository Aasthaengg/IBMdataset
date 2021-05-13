x, y = map(int, input().split())
ans = float("inf")
rx, ry = -x, -y
# 最初にBを押して、最後に押す場合
if rx <= ry:
    ans = min(ans, ry-rx + 2)
# 最初にBを押して、最後に押さない場合
if rx <= y:
    ans = min(ans, y - rx + 1)
# 最初にBを押さず、最後に押す場合
if x <= ry:
    ans = min(ans, ry - x + 1)
# 最初にBを押さず、最後に押さない場合
if x <= y:
    ans = min(ans, y - x)
print(ans)