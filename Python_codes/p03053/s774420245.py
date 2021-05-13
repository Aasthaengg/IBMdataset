H,W = list(map(int,input().split()))
M = []
for i in range(H):
    M.append(list(input()))

Bs = []
for i in range(H):
    for j in range(W):
        if M[i][j]=="#":
            Bs.append([i,j])

from collections import deque
memo = [[2000] * W for i in range(H)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
que = deque([])
que.append(Bs)
for Bi,Bj in Bs:
    memo[Bi][Bj] = 0

out = 0
while que:
    ps = que.popleft()
    next = []
    for p in ps:
        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]
            if (0<=nx<W)and(0<=ny<H)and(memo[ny][nx]==2000):
                next.append((ny, nx))
                memo[ny][nx] = memo[p[0]][p[1]] + 1
                if memo[ny][nx]>out:
                    out=memo[ny][nx]
    if len(next)>0:
        que.append(next)

print(out)