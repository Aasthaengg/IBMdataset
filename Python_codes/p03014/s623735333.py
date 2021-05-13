def main():
    H, W = map(int, input().split())
    g = [str(input()) for _ in range(H)]
    LW = [[0] * W for _ in range(H)]
    LH = [[0] * W for _ in range(H)]
    for h in range(H):
        cnt = 0
        for w in range(W):
            if g[h][w] == '.':
                cnt += 1
            else:
                for i in range(1, cnt+1):
                    LW[h][w-i] = cnt
                LW[h][w] = 0
                cnt = 0
        else:
            for i in range(cnt):
                LW[h][w-i] = cnt
    for w in range(W):
        cnt = 0
        for h in range(H):
            if g[h][w] == '.':
                cnt += 1
            else:
                for i in range(1, cnt+1):
                    LH[h-i][w] = cnt
                LH[h][w] = 0
                cnt = 0
        else:
            for i in range(cnt):
                LH[h-i][w] = cnt
    ans = 0
    for h in range(H):
        for w in range(W):
            if g[h][w] != '#':
                ans = max(ans, LH[h][w] + LW[h][w] - 1)
    print(ans)
main()