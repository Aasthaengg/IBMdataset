h, w, m = map(int, input().split())
h_cnt = [0 for _ in range(h)]
w_cnt = [0 for _ in range(w)]
xs = []
ys = []
for _ in range(m):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    h_cnt[y] += 1
    w_cnt[x] += 1
    xs.append(x)
    ys.append(y)
h_max = max(h_cnt)
w_max = max(w_cnt)
h_max_induce = {i: v for i, v in enumerate(h_cnt) if v == h_max}
w_max_induce = {i: v for i, v in enumerate(w_cnt) if v == w_max}

cnt = 0
for i in range(m):
    x = xs[i]
    y = ys[i]
    if x in w_max_induce and y in h_max_induce:
        cnt += 1
if cnt == len(h_max_induce.keys())*len(w_max_induce.keys()):
    print(h_max+w_max-1)
else:
    print(h_max+w_max)


