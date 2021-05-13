[n,m] = [int(i) for i in input().split()]
ans = 0
ab = []
stage = [[0] * n for i in range(n)]
for i in range(m):
    ab.append([int(j)-1 for j in input().split()])
    stage[ab[-1][0]][ab[-1][1]] = 1
    stage[ab[-1][1]][ab[-1][0]] = 1
for i in range(m):
    visit = [0] * n
    now = 0
    stage[ab[i][0]][ab[i][1]] = 0
    stage[ab[i][1]][ab[i][0]] = 0
    next = [0]
    while len(next):
        now = next.pop()
        visit[now] = 1
        for j in range(n):
            if stage[now][j] == 1 and visit[j] != 1:
                next.append(j)

    stage[ab[i][0]][ab[i][1]] = 1
    stage[ab[i][1]][ab[i][0]] = 1



    if 0 in visit:
        ans += 1
print(ans)
