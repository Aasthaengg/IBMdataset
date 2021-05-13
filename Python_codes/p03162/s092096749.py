n = int(input())
points = [list(map(int, input().strip().split())) for i in range(n)]
dp = [points[0]]

for i in range(1, n):
    dp.append([
        max(dp[-1][1] + points[i][0], dp[-1][2] + points[i][0]),
        max(dp[-1][0] + points[i][1], dp[-1][2] + points[i][1]),
        max(dp[-1][0] + points[i][2], dp[-1][1] + points[i][2]),
        ])

print(max(dp[-1]))

