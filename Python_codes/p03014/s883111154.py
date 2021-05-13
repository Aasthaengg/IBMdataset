def main():
    H, W = (int(_) for _ in input().split())
    S = [input() for _ in range(H)]
    yoko = [[0] * W for _ in range(H)]
    tate = [[0] * W for _ in range(H)]

    for i in range(H):
        right = 0
        cc = 0
        for left in range(W):
            if S[i][left] == '#':
                cc = 0
                right += 1
                continue
            while right < W and S[i][right] == '.':
                right += 1
            cc = right - left
            if left > 0 and S[i][left-1] == '.': yoko[i][left] = yoko[i][left-1]
            else: yoko[i][left] = cc
    for i in range(W):
        bottom = 0
        cc = 0
        for top in range(H):
            if S[top][i] == '#':
                cc = 0
                bottom += 1
                continue
            while bottom < H and S[bottom][i] == '.':
                bottom += 1
            cc = bottom - top
            if top > 0 and S[top-1][i] == '.': tate[top][i] = tate[top-1][i]
            else: tate[top][i] = cc
    output = 0
    for i in range(H):
        for j in range(W):
            output = max(output, yoko[i][j]+tate[i][j]-1)
    print(output)
    return

if __name__ == '__main__':
    main()
