N, M, K = map(int, input().split(' '))
A_ls = [0] + list(map(int, input().split(' ')))
B_ls = [0] + list(map(int, input().split(' ')))

for i in range(1, N+1):
    A_ls[i] += A_ls[i - 1]

for i in range(1, M+1):
    B_ls[i] += B_ls[i - 1]

a_cnt, b_cnt, rst = 0, M, 0
while a_cnt < N + 1:
    if A_ls[a_cnt] > K:
        break
    while A_ls[a_cnt] + B_ls[b_cnt] > K and b_cnt > 0:
        b_cnt -= 1
    rst = max(rst, a_cnt + b_cnt)
    a_cnt += 1
print(rst)