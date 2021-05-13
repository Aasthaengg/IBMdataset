H, W, K = map(int, input().split())
L = [list(input()) for _ in range(H)]
ans = 0

for h_p in range(2 ** H):
    for w_p in range(2 ** W):
        count = 0
        for h in range(H):
            for w in range(W):
                if (h_p >> h) & 1 == 0 and (w_p >> w) & 1 == 0:
                    if (L[h][w] == '#'):
                        count += 1
        if count == K:
            ans += 1

print(ans)
