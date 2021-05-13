H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]
ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        cnt = 0
        for x in range(H):
            for y in range(W):
                if (i>>x)&1==1 and (j>>y)&1 and c[x][y] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)

