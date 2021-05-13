def main():
    H, W = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    flag = True

    for i in range(H):
        for j in range(W):
            if s[i][j] == ".":
                continue

            cnt = 0
            for k in range(4):
                x = j + dx[k]
                y = i + dy[k]
                if x >= 0 and x < W and y >= 0 and y < H:
                    if s[y][x] == "#":
                        cnt += 1

            if cnt == 0:
                flag = False

    if flag == True:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
