H, W = map(int, input().split())
d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
G = [list(input()) for _ in range(H)]
ans = [[""] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if G[i][j] == '#':
            ans[i][j] = '#'
            continue
        cnt = 0
        for dx, dy in d:
            ni = i + dx
            nj = j + dy
            if ni < 0 or H <= ni or nj < 0 or W <= nj:
                continue
            if G[ni][nj] == '#':
                cnt += 1
        ans[i][j] = str(cnt)
for a in ans:
    print(''.join(a))
