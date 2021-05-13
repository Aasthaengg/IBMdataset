H, W, M = map(int, input().split())
HW = set(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M))

sum_h = [0]*H; sum_w = [0]*W
for h, w in HW:
    sum_h[h] += 1
    sum_w[w] += 1

max_h_num = 0
h_num_ix = {}
for i in range(H):
    num = sum_h[i]
    if num == 0: continue
    if not num in h_num_ix: h_num_ix[num] = set()
    h_num_ix[num].add(i)
    max_h_num = max(max_h_num, num)

max_w_num = 0
w_num_ix = {}
for i in range(W):
    num = sum_w[i]
    if num == 0: continue
    if not num in w_num_ix: w_num_ix[num] = set()
    w_num_ix[num].add(i)
    max_w_num = max(max_w_num, num)

max_num = max_h_num + max_w_num - 1
for h_ix in h_num_ix[max_h_num]:
    for w_ix in w_num_ix[max_w_num]:
        if (h_ix, w_ix) in HW: continue
        print(max_num + 1)
        exit()
print(max_num)
