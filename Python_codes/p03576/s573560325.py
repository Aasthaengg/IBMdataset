import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]
xy = []
for _ in range(n):
    xy.append([int(x) for x in input().split()])
ans = float('inf')
xy.sort()
for i in range(n):
    left = xy[i][0]
    y = [xy[i][1]]
    for j in range(i + 1, n):
        right = xy[j][0]
        y.append(xy[j][1])
        y.sort()
        if j - i + 1 < k:
            continue
        for p in range(len(y)):
            bottom = y[p]
            for q in range(len(y)):
                if q - p + 1 < k:
                    continue
                top = y[q]
                ans = min(ans, (right - left)*(top - bottom))
print(ans)
