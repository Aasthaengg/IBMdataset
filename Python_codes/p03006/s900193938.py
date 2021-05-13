n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
s_xy = set(xy)

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        p, q = xy[j][0] - xy[i][0], xy[j][1] - xy[i][1]
        count = max(count, sum((x-p,y-q) in s_xy for x, y in s_xy))

print(n - count)
