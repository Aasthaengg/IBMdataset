S = input()
N = len(S)
mod = 10**9+7

A_cum = [0] * N
C_cum = [0] * N
q_sum_left = [0] * N
q_sum_right = [0] * N
for i in range(N - 1):
    s = S[i]
    if s == 'A':
        A_cum[i + 1] = A_cum[i] + 1
    else:
        A_cum[i + 1] = A_cum[i]
    if s == '?':
        q_sum_left[i + 1] = q_sum_left[i] + 1
    else:
        q_sum_left[i + 1] = q_sum_left[i]
for i in range(N - 1, 0, -1):
    s = S[i]
    if s == 'C':
        C_cum[i - 1] = C_cum[i] + 1
    else:
        C_cum[i - 1] = C_cum[i]
    if s == '?':
        q_sum_right[i - 1] = q_sum_right[i] + 1
    else:
        q_sum_right[i - 1] = q_sum_right[i]
ans = 0
for i in range(N):
    if S[i] == 'B' or S[i] == '?':
        ans = (ans + (A_cum[i] * pow(3, q_sum_left[i], mod) + q_sum_left[i] * pow(3, max(0, q_sum_left[i] - 1), mod))
               * (C_cum[i] * pow(3, q_sum_right[i], mod) + q_sum_right[i] * pow(3, max(0, q_sum_right[i] - 1), mod))) % mod

print(ans)
