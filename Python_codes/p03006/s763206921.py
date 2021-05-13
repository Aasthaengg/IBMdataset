N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

pq = []
for i in range(N):
    for j in range(N):
        if i != j:
            x1 = xy[i][0]
            y1 = xy[i][1]
            x2 = xy[j][0]
            y2 = xy[j][1]
            pq.append((x2 - x1, y2 - y1))

ans = N
for p,q in pq:
    tmp = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                x1 = xy[i][0]
                y1 = xy[i][1]
                x2 = xy[j][0]
                y2 = xy[j][1]
                if x2 - x1 == p and y2 - y1 == q:
                    tmp += 1
    ans = min(ans, N - tmp)

print(ans)
