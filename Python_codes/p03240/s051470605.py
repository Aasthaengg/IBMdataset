n = int(input())
xyh = []
inf = 10 ** 10
for _ in range(n):
    x, y, h = map(int, input().split())
    xyh.append((x, y, h))
xyh.sort(key=lambda x:x[2], reverse=True)

# 全ての中央座標の組み合わせを試す
for i in range(101):
    for j in range(101):
        x, y, h = xyh[0]
        H = h + abs(i-x) + abs(j-y)
        for x, y, h in xyh:
            if h != max(H - abs(i-x) - abs(j-y), 0):
                break
        else:
            ans = i, j, H
print(*ans)