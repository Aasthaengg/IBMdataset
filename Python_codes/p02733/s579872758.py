


H,W,K = map(int, input().split())
S = [[int(i) for i in list(input())] for _ in range(H)]

accum_col = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0:
            accum_col[i][j] = S[i][j]
        else:
            accum_col[i][j] = accum_col[i-1][j] + S[i][j]

def cnt_white(x, a, b):
    if a == 0:
        return accum_col[b-1][x]
    else:
        return accum_col[b-1][x] - accum_col[a-1][x]

ans = H*W
for bit in range(1 << (H-1)):
    # 横に直線で割るが、その線の真下のindex
    horizs = [0]
    cnt_split = bin(bit).count("1")
    for i in range(H-1):
        if bit & (1 << i):
            """
            i=0でbitに1が立っていると、y=0と1の間を横一直線に割るので、次のブロックの始まりはy=1から。
            みたいな意味でi+1
            """
            horizs.append(i+1)
    
    horizs.append(H)
    # horizsの要素間がブロックなので-1
    # これまでの各ブロックの累積のホワイトチョコの個数
    prev = [0] * (len(horizs) - 1)
    for x in range(W):
        # 横位置でxの列の各ブロックのホワイトチョコの個数
        curr_col = [cnt_white(x, a, b) for a,b in zip(horizs, horizs[1:])]
        # 各ブロックの個数
        prev_curr = [curr_col[i] + prev[i] for i in range(len(horizs)-1)]
        if max(curr_col) > K:
            # 一行だけみてもKを超えるブロックがあるので、十分大きい値を足してアウトにする
            cnt_split += H*W
            break
        if max(prev_curr) > K:
            # ホワイトチョコが最も多いブロックでKを超えていれば、手前の列までで割る
            prev = curr_col
            cnt_split += 1
        else:
            # いずれもK以下であればそのままブロックを広げる
            prev = prev_curr
    
    ans = min(ans, cnt_split)

print(ans)
