H, W, K = map(int, input().split())
S = [list(map(int, input())) for i in range(H)]

ret = W - 1 + H - 1

for i in range(1 << (H - 1)):
    sep = bin(i)[2:].rjust(H - 1, '0')[::-1]

    tile_idx = [0] * H
    cut = 0

    for j in range(H):
        tile_idx[j] = cut

        if j == H - 1:
            break

        if sep[j] == '1':
            cut += 1

    cnt_lst = [0] * (cut + 1)
    num_cnt = 0

    for w in range(W):
        col_new = [0] * (cut + 1)

        flag = False
        flag1 = False
        for h in range(H):
            if S[h][w] == 1:
                idx = tile_idx[h]
                col_new[idx] += 1

        for a in col_new:
            if a > K:
                flag1 = True
                break

        if flag1:
            break

        for k in range(cut + 1):
            if cnt_lst[k] + col_new[k] > K:
                num_cnt += 1
                for l in range(cut + 1):
                    cnt_lst[l] = col_new[l]

                flag = True
                break

        if not flag:
            for k in range(cut + 1):
                cnt_lst[k] += col_new[k]

    if not flag1:
        ret = min(ret, num_cnt + cut)


print(ret)
