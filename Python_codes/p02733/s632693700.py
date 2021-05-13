
from bisect import bisect_left

H,W,K = map(int, input().split())
S = [input() for _ in range(H)]

"""
H <= 10までなので、横直線方向の割り方を全探索できそう
縦直線方向の割り方は貪欲か。
横直線の割方が決まったら、次は縦に割っていくが、ブロックの横幅を1にしても、ブロックないのホワイトチョコがKを超える場合もありうるので、その場合は、その横直線の割り方で条件を満たすことはできない


H=1や W=1の場合は普通に貪欲で。
"""


def is_over_K(lst, block_num):
    res = False
    for i in range(block_num):
        if lst[i] > K:
            res = True
            break
    return res


if H != 1 and W != 1:
    # 全区切りで割った場合が最大
    ans = (H-1) + (W-1)
    for bit in range(1 << (H-1)):
        can_split_h = True
        cnt_split_h = bin(bit).count("1")
        cnt_split_w = 0

        # 横直線方向で割る場合は、その箇所のindexを保持
        if cnt_split_h >= 1:
            idx_split_h = []
            for i in range(H-1):
                if bit & (1 << i):
                    idx_split_h.append(i)

        cnt_blocks = cnt_split_h + 1
        cnt_whites = [0] * (cnt_blocks)
        ex_cnt_whites = [0] * (cnt_blocks)

        for x in range(W):
            for y in range(H):
                if S[y][x] == "1":
                    if cnt_blocks > 1:
                        block_num = bisect_left(idx_split_h, y)
                    else:
                        block_num = 0

                    cnt_whites[block_num] += 1
            
            # それぞれKを超えていないか確認
            is_over = is_over_K(cnt_whites, cnt_blocks)

            
            if not is_over:
                # Kを超えないので、さらにxを追加して見ていく
                # xまでで各ブロックでホワイトチョコがいくつあるか保持（次のxでKを超えた場合に、差分を利用するので）
                for i in range(cnt_split_h+1):
                    ex_cnt_whites[i] = cnt_whites[i]
            else:
                # Kを超えるのでxの左の縦直線でわる
                cnt_split_w += 1
                # xの左の縦直線で割った場合のホワイトチョコの個数を求める（現在のxのみの個数）
                for i in range(cnt_blocks):
                    cnt_whites[i] -= ex_cnt_whites[i]
                    ex_cnt_whites[i] = cnt_whites[i]

                # 一列だけにしてもKを超えるなら、その横直線の分割はできない
                if is_over_K(cnt_whites, cnt_blocks):
                    can_split_h = False
                    break
            # 一列だけにしてもKを超えるブロックがあるので、この横直線の分割はできない
            if not can_split_h:
                break
        
        if can_split_h:
            ans = min(ans, cnt_split_h + cnt_split_w)

# H=1, W=1の場合忘れとった...
elif H == 1:
    ans = 0
    cnt = 0
    for i in range(W):
        if S[0][i] == "1":
            cnt += 1
        if cnt > K:
            ans += 1
            cnt = 1
else:
    ans = 0
    cnt = 0
    for i in range(H):
        if S[i][0] == "1":
            cnt += 1
        if cnt > K:
            ans += 1
            cnt = 1

print(ans)