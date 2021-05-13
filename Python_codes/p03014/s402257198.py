def main():
    H, W = (int(i) for i in input().split())
    A = [input() for i in range(H)]
    L = [[[0]*W for _ in range(H)] for _ in range(4)]
    for di in range(4):
        if di == 0 or di == 1:
            rangeH = range(H)
            rangeW = range(W)
        else:
            rangeH = range(H)[::-1]
            rangeW = range(W)[::-1]

        for h in rangeH:
            for w in rangeW:
                if A[h][w] == "#":
                    continue
                if di == 0:
                    if h-1 < 0 or A[h-1][w] == "#":
                        L[di][h][w] = 1
                    else:
                        L[di][h][w] = L[di][h-1][w] + 1
                elif di == 1:
                    if w-1 < 0 or A[h][w-1] == "#":
                        L[di][h][w] = 1
                    else:
                        L[di][h][w] = L[di][h][w-1] + 1
                elif di == 2:
                    if h+1 > H-1 or A[h+1][w] == "#":
                        L[di][h][w] = 1
                    else:
                        L[di][h][w] = L[di][h+1][w] + 1
                elif di == 3:
                    if w+1 > W-1 or A[h][w+1] == "#":
                        L[di][h][w] = 1
                    else:
                        L[di][h][w] = L[di][h][w+1] + 1
    ans = 0
    for h in range(H):
        for w in range(W):
            v = sum(L[i][h][w] for i in range(4)) - 3
            ans = max(ans, v)
    print(ans)


if __name__ == '__main__':
    main()
