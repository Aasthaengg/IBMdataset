H,W,K = map(int, input().split())
C = []
for i in range(H):
    C.append(list(input()))
ans = 0

for maskH in range(1<<H):
    for maskW in range(1<<W):
        black = 0
        for i in range(H):
            for j in range(W):
                #両方のmaskが0の時だけ、'#'ならblack++する
                if maskH&(1<<i) and maskW&(1<<j) and C[i][j]=='#':
                    black += 1
        if black == K:
            ans += 1

print(ans)