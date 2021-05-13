
def main():
    H,W,K = map(int, input().split())
    table = [list(input()) for _ in range(H)]

    res = [[0] * W for _ in range(H)]

    cnt = 0
    for h in range(H):
        line_flg = False
        for w in range(W):
            c = table[h][w]
            if c == "#":
                cnt += 1
                line_flg = True
            if line_flg:
                res[h][w] = cnt

    for h in range(H):
        for w in list(range(W-1))[::-1]:
            if res[h][w] == 0:
                res[h][w] = res[h][w+1]

    for h in range(1,H):
        for w in range(W):
            if res[h][w] == 0:
                res[h][w] = res[h-1][w]

    for h in list(range(H-1))[::-1]:
        for w in range(W):
            if res[h][w] == 0:
                res[h][w] = res[h+1][w]

    for l in res:
        print(*l)
if __name__ == "__main__":
    main()