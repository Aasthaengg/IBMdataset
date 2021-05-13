# input
N = int(input())
S = input()

# check

# 参考：https://qiita.com/IGMML/items/5aa36f7fa03746ed6e6c
# 累積和で求める
int_s = [0] * N
cum_sum_w = [0] * (N + 1)
cum_sum_e = [0] * (N + 1)
answers = [0] * N

for i in range(N):
    if S[i] == 'W':
        int_s[i] = 1
    else:
        int_s[i] = 0
    cum_sum_w[i + 1] = cum_sum_w[i] + int_s[i]

for i in range(N):
    if S[i] == 'E':
        int_s[i] = 1
    else:
        int_s[i] = 0
    cum_sum_e[i + 1] = cum_sum_e[i] + int_s[i]

for i in range(N):
    answers[i] = cum_sum_w[i] + (cum_sum_e[N] - cum_sum_e[i + 1])
    
print(min(answers))