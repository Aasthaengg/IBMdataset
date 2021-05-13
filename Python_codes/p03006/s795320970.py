n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(n - 1):
    xi, yi = xy[i]
    for j in range(i + 1, n):
        xj, yj = xy[j]
        cost = 0
        for x, y in xy:
            cost += 1 if [x - xj + xi, y - yj + yi] in xy else 0
    cnt = max(cnt, cost)
print(n - cnt)