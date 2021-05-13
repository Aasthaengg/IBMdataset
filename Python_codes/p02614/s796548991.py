H, W, K = map(int, input().split())
a = [input() for i in range(H)]
ans = 0
for i in range(1 <<H):
    for j in range(1 <<W):
        black = 0
        for k in range(H):
            for l in range(W):
                if (i >>k)&1 ==0 and (j >>l)&1 == 0 and a[k][l] == '#':
                    black += 1
        if black == K:
            ans += 1
print(ans)