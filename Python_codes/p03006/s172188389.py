n = int(input())

points = [list(map(int, input().split(" "))) for _ in range(n)]
X = 0
Y = 1
ans = 10 ** 14
if n == 1:
    ans = 1
else:
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            x1, y1 = points[i]
            x2, y2 = points[j]
            p = x1 - x2
            q = y1 - y2
            cost = n
            for point1 in points:  # そのpointからcost0で遷移できる先があるかどうか
                fromx, fromy = point1
                for point2 in points:
                    tox, toy = point2
                    if fromx - tox == p and fromy - toy == q:
                        cost -= 1
                        break
            if ans > cost:
                ans = cost
print(ans)



