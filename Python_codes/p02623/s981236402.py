N, M, K = map(int, input().split(' '))
A_ls = [0] + list(map(int, input().split(' ')))
for i in range(N):
    A_ls[i + 1] += A_ls[i]
B_ls = [0] + list(map(int, input().split(' ')))
for i in range(M):
    B_ls[i + 1] += B_ls[i]
b_cnt, rst = M, 0
for a_cnt in range(N + 1):
    if A_ls[a_cnt] > K:
        break
    while A_ls[a_cnt] + B_ls[b_cnt] > K and b_cnt >= 0:
        b_cnt -= 1
    rst = max(rst, a_cnt + b_cnt)
print(rst)