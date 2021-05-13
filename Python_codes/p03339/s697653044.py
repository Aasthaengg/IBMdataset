# -*- coding: utf-8 -*-
n = int(input())
ln = list(map(int, input().replace('W', '0 ').replace('E', '1 ').split()))

# 先頭だけ先に計算（do-while相当）
w_sum = 0                           # 西側で振り返る人
sum_min = e_sum = sum(ln) - ln[0]   # 東側で振り返る人

for i in range(1, n-1):
    #sum_min = min(sum_min, sum(ln[i+1:n]) + (i - sum(ln[0:i])))
    w_sum += 1 if ln[i-1] == 0 else 0
    e_sum -= ln[i]
    sum_min = min(sum_min, w_sum + e_sum)

# 末尾も個別に計算
else:
    w_sum += 1 if ln[n-1] == 0 else 0
    sum_min = min(sum_min, w_sum)


print(sum_min)
