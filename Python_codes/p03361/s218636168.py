LI = lambda: list(map(int, input().split()))

H, W = LI()
S = [input() for _ in range(H)]


def main():
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                continue
            if j > 0 and S[i][j - 1] == "#":
                continue
            if j < W - 1 and S[i][j + 1] == "#":
                continue
            if i > 0 and S[i - 1][j] == "#":
                continue
            if i < H - 1 and S[i + 1][j] == "#":
                continue
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
