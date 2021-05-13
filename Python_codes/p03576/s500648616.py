N, K = map(int, input().split(' '))
points = [tuple(map(int, input().split(' '))) for _ in range(N)]
points.sort()

ans = float('inf')
for i in range(N):
    for j in range(i + K - 1, N):
        xmin, xmax = points[i][0], points[j][0]
        que = []
        for k in range(N):
            if xmin <= points[k][0] <= xmax:
                que.append(points[k][1])
        if len(que) >= K:
            que.sort()
            for k in range(len(que) - K + 1):
                ans = min(ans, (max(que[k: k + K]) - min(que[k: k + K])) * (xmax - xmin))
print(ans)