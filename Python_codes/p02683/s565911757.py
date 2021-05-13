N, M, X = map(int, input().split(' '))
price, exp, rst = [], [ []  for i in range(N) ], -1
for i in range(N):
    ls = list(map(int, input().split(' ')))
    price.append(ls[0])
    exp[i] = ls[1:]
for i in range(1 << N):
    price_combi, exp_combi, sum_exp, ls_cnt = [], [], [0] * M, []
    for j in range(N):
        if i >> j & 1:
            price_combi.append(price[j])
            exp_combi.append(exp[j])
    for s in exp_combi:
        for t in range(M):
            sum_exp[t] += s[t]
    [ ls_cnt.append(x) for x in sum_exp if x >= X ]
    if len(ls_cnt) == M:
        if rst == -1:
            rst = sum(price_combi)
        else:
            rst = min(rst, sum(price_combi))
print(rst)