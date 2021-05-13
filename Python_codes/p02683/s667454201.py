
N, M, X = map(int, input().split(' '))
price, exp = [], [ [] for i in range(N) ]
rst = -1
for i in range(N):
    ls = list(map(int, input().split(' ')))
    price.append(ls[0])
    exp[i] = ls[1:]
for i in range(1 << N):
    price_comb, exp_comb, exp_sum, cnt_ls = [], [], [0] * M, []
    for j in range (N):
        if i >> j & 1:
            price_comb.append(price[j])
            exp_comb.append(exp[j])
    for s in exp_comb:
        for t in range(M):
            exp_sum[t] += s[t]
    cnt_ls = [ x for x in exp_sum if x >= X ]
    if len(cnt_ls) == M:
        if rst == -1:
            rst = sum(price_comb)
        else:
            rst = min(rst, sum(price_comb))
print(rst)