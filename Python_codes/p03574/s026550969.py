def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue

            cnt = 0
            for k in range(8):
                x = j + dx[k]
                y = i + dy[k]
                if x >= 0 and x < W and y >= 0 and y < H:
                    if S[y][x] == "#":
                        cnt += 1

            S[i][j] = str(cnt)

    for i in range(H):
        print("".join(S[i]))


if __name__ == "__main__":
    main()
