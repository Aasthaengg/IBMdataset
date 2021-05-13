S = input()

len_S = len(S)
for i in range(1, len_S):
    if i % 2 == 0:
        tmp_S = S[:len_S - i]
        n_half = len(tmp_S) // 2
        S_l = tmp_S[:n_half]
        S_r = tmp_S[n_half:]
        if S_l == S_r:
            break
print(len(tmp_S))