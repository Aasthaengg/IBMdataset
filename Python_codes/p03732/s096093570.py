from itertools import accumulate
N, W = map(int, input().split())
w0, w1, w2, w3 = [], [], [], []
base_w = -1
for i in range(N):
    w, v = map(int, input().split())
    if base_w < 0:
        base_w = w

    # 重みごとの箱にいれる
    w -= base_w
    if w == 0:
        w0.append(v)
    elif w == 1:
        w1.append(v)
    elif w == 2:
        w2.append(v)
    else:
        w3.append(v)

# 降順ソート
w0.sort(reverse=True)
w1.sort(reverse=True)
w2.sort(reverse=True)
w3.sort(reverse=True)

# 累積和
w0 = [0] + list(accumulate(w0))
w1 = [0] + list(accumulate(w1))
w2 = [0] + list(accumulate(w2))
w3 = [0] + list(accumulate(w3))

ans = 0
for i0 in range(len(w0)):
    for i1 in range(len(w1)):
        for i2 in range(len(w2)):
            for i3 in range(len(w3)):
                if base_w * i0 + (base_w + 1) * i1 + (base_w + 2) * i2 + (base_w + 3) * i3 > W:
                    continue
                ans = max(ans, w0[i0] + w1[i1] + w2[i2] + w3[i3])

print(ans)
