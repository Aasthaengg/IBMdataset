# 解答AC

x,y = map(int, input().split())

ans = float("inf")
for B1 in range(2):
    x2 = -x if B1 else x
    for B2 in range(2):
        y2 = -y if B2 else y
        if x2 <= y2:
            ans = min(ans, y2 - x2 + B1 + B2)

print(ans)