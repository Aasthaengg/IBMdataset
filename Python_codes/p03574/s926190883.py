def main():
    H, W = map(int, input().split())
    S = [["*" for _ in range(W + 2)] for _ in range(H + 2)]
    for i in range(1, H + 1):
        S[i][1: W + 1] = input()

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if S[i][j] == "#":
                continue

            cnt = 0
            if S[i - 1][j - 1] == "#":
                cnt += 1
            if S[i - 1][j] == "#":
                cnt += 1
            if S[i - 1][j + 1] == "#":
                cnt += 1
            if S[i][j - 1] == "#":
                cnt += 1
            if S[i][j + 1] == "#":
                cnt += 1
            if S[i + 1][j - 1] == "#":
                cnt += 1
            if S[i + 1][j] == "#":
                cnt += 1
            if S[i + 1][j + 1] == "#":
                cnt += 1

            S[i][j] = str(cnt)

    for i in range(1, H + 1):
        print("".join(S[i][1: W + 1]))


if __name__ == "__main__":
    main()
