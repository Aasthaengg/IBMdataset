from itertools import accumulate
N, W = map(int, input().split())
Item = [[] for i in range(4)]
for i in range(N):
    wi, vi = map(int, input().split())
    if i == 0:
        Item[0].append(vi)
        w_base = wi
    else:
        Item[wi - w_base].append(vi)

w0, w1, w2, w3 = Item
w0 = [0] + list(accumulate(sorted(w0, reverse=True)))
w1 = [0] + list(accumulate(sorted(w1, reverse=True)))
w2 = [0] + list(accumulate(sorted(w2, reverse=True)))
w3 = [0] + list(accumulate(sorted(w3, reverse=True)))

ans = 0
for i in range(len(w0)):
    for j in range(len(w1)):
        for k in range(len(w2)):
            tmp_weight = w_base * i + (w_base + 1) * j + (w_base + 2) * k
            if tmp_weight > W:
                continue
            tmp_ans = w0[i] + w1[j] + w2[k] + w3[min((W - tmp_weight) // (w_base + 3), len(w3) - 1)]
            ans = max(ans, tmp_ans)

print(ans)
