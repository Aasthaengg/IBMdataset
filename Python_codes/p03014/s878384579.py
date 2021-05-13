def main():
    H, W = map(int, input().split())
    A = [list(input()) for i in range(H)]
    right = [[0] * W for _ in range(H)]
    left = [[0] * W for _ in range(H)]
    upper = [[0] * W for _ in range(H)]
    under = [[0] * W for _ in range(H)]

    num_max_loc = 0

    for i in range(H):
        tmp_num = 0
        for j in range(W):
            if A[i][j] == "#":
                tmp_num = 0
            else:
                tmp_num += 1
                left[i][j] = tmp_num

    for i in range(H):
        tmp_num = 0
        for j in range(W-1, -1, -1):
            if A[i][j] == "#":
                tmp_num = 0
            else:
                tmp_num += 1
                right[i][j] = tmp_num

    for i in range(W):
        tmp_num = 0
        for j in range(H):
            if A[j][i] == "#":
                tmp_num = 0
            else:
                tmp_num += 1
                upper[j][i] = tmp_num

    for i in range(W):
        tmp_num = 0
        for j in range(H-1, -1, -1):
            if A[j][i] == "#":
                tmp_num = 0
            else:
                tmp_num += 1
                under[j][i] = tmp_num

    for i in range(H):
        for j in range(W):
            tmp_sum = (
                left[i][j] + right[i][j] + upper[i][j] + under[i][j] - 3)
            num_max_loc = max(num_max_loc, tmp_sum)

    print(num_max_loc)


if __name__ == '__main__':
    main()
