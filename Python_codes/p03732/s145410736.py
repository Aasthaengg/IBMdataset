from itertools import accumulate
N, W_limit = map(int, input().split())
W, V = [], []
for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# 基準となるW
base_W = W[0]
# 0 ~ 3の範囲に調節
W = [w - base_W for w in W]

# 重みごとに商品を分ける
Items = [[] for i in range(4)]
for w, v in zip(W, V):
    Items[w].append(v)

# 降順ソートして累積和を取っておく
Items = [[0] + sorted(x, reverse=True) for x in Items]
Items = [list(accumulate(x)) for x in Items]

# それぞれの重さから何個選ぶかで全探索
ans = 0
for w0 in range(len(Items[0])):
    for w1 in range(len(Items[1])):
        for w2 in range(len(Items[2])):
            for w3 in range(len(Items[3])):
                tmp_W = (w0 * base_W) + (w1 * (base_W + 1)) + (w2 * (base_W + 2)) + (w3 * (base_W + 3))
                if tmp_W > W_limit:
                    continue
                tmp_V = Items[0][w0] + Items[1][w1] + Items[2][w2] + Items[3][w3]
                ans = max(ans, tmp_V)

print(ans)
