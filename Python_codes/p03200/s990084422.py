S = input()

b_cnt = 0
C = [0] * len(S)
for i in range(len(S)):
    if S[i] == 'B':
        # 白の個数+1
        b_cnt += 1
    if S[i] == 'W':
        # それまでにあった白の個数を記録
        C[i] = b_cnt

print(sum(C))
