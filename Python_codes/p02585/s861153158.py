N, K = map(int, input().split())
P = [int(i) - 1 for i in input().split()]
C = [int(i) for i in input().split()]

points = list()
for i in range(N):
    sum = 0
    now = P[i]
    result = list()
    flag = True
    for j in range(N):
        sum += C[now]
        result.append(sum)
        if now == i:
            break
        if j == N-1 and now != i:
            flag = False
        now = P[now]

    if flag:
        points.append(result)
    else:
        # iスタートでiに戻るループが存在しない
        points.append([-int(1e19)])

ans = -int(1e19)

for i in range(len(points)):
    now = i
    tmpp = 0
    k = K
    while points[now][0] == -int(1e19):
        now = P[now]
        tmpp += C[now]
        k -= 1
        ans = max(ans, tmpp)

    cir = len(points[now])
    cir_point = points[now][cir-1]

    if k <= cir:
        for j in range(k):
            ans = max(ans, points[now][j] + tmpp)
    else:
        if cir_point > 0:
            lm = k // cir - 1
            for j in range(cir):
                ans = max(ans, points[now][j] + lm * cir_point + tmpp)
            for j in range(k % cir):
                ans = max(ans, points[now][j] + (lm + 1) * cir_point + tmpp)
        else:
            for j in range(cir):
                ans = max(ans, points[now][j] + tmpp)

print(ans)