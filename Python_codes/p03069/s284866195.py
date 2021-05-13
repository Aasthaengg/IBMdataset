N = int(input())
S = input()

b_from_l = [0 for _ in range(N)]
w_from_r = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        if S[i] == '#':
            b_from_l[i] = 1
    else:
        if S[i] == '#':
            b_from_l[i] = b_from_l[i - 1] + 1
        else:
            b_from_l[i] = b_from_l[i - 1]

for i in range(N - 1, -1, -1):
    if i == N - 1:
        if S[i] == '.':
            w_from_r[i] = 1
    else:
        if S[i] == '.':
            w_from_r[i] = w_from_r[i + 1] + 1
        else:
            w_from_r[i] = w_from_r[i + 1]

ans = min(S.count('.'), S.count('#'))
for i in range(N - 1):
    ans = min(ans, b_from_l[i] + w_from_r[i + 1])
print(ans)
