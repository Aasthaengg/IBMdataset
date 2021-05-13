
def main():
    H,W = list(map(int, input().split()))
    S = [input() for _ in range(H)]

    count_h = [[0] * W for _ in range(H)]
    count_w = [[0] * W for _ in range(H)]

    tmp_cnt_h = [0] * W
    for i in range(H):
        w_cnt = 0
        for j,c in enumerate(S[i]):
            if c == '.':
                tmp_cnt_h[j] += 1
                w_cnt += 1
            else:
                count_w[i][j-w_cnt:j] = [w_cnt]*w_cnt
                w_cnt = 0

                h_cnt = tmp_cnt_h[j]
                for x in range(i-h_cnt,i):
                    count_h[x][j] = h_cnt
                tmp_cnt_h[j] = 0

        count_w[i][W-w_cnt:W] = [w_cnt]*w_cnt

    for i, h_cnt in enumerate(tmp_cnt_h):
        for x in range(H-h_cnt,H):
            count_h[x][i] = h_cnt

    max_light = 0
    for i in range(H):
        for j in range(W):
            max_light = max(max_light, count_h[i][j] + count_w[i][j])
    print(max_light-1)

if __name__ == "__main__":
    main()