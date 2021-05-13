N, K = map(int, input().split())
S = input()

zero = []
tmp_zero_cnt = 0
tmp_zero_idx = -1
for i in range(N):
    if S[i] == "0":
        if tmp_zero_cnt == 0:
            tmp_zero_idx = i
        tmp_zero_cnt += 1
    else:
        if tmp_zero_cnt != 0:
            zero.append([tmp_zero_idx, tmp_zero_cnt])
            tmp_zero_cnt = 0
if tmp_zero_cnt != 0:
    zero.append([tmp_zero_idx, tmp_zero_cnt])

if len(zero) <= K:
    print(N)
else:
    zero = [[-1, 1]] + zero + [[N, 1]]
    M = len(zero)
    ans = 0
    for i in range(1, M - K):
        num = (zero[i + K][0] - 1) - (zero[i - 1][0] + zero[i - 1][1]) + 1
        if num > ans:
            ans = num
    print(ans)
