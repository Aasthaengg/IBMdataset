S = input()
N = len(S)

ans = [0] * N

tmp_l = -1

def compute_right(index):
    org = index
    tmp = S[index]
    while tmp != 'R' and index < N - 1:
        index += 1
        tmp = S[index]
    if index == N - 1:
        index = N
    return index - org

for i in range(N):
    if i < N - 1 and S[i] == S[i+1] and S[i] == 'R':
        continue
    if i > 0 and S[i] == S[i-1] and S[i] == 'L':
        tmp_l = i
        continue
    if S[i] == 'L':
        left = (i - tmp_l - 1) // 2
        right = (compute_right(i) - 1) // 2
        ans[i] = 1 + left + right
        tmp_l = i
    if S[i] == 'R':
        left = (i - tmp_l - 1) // 2
        right = compute_right(i + 1) // 2
        ans[i] = 1 + left + right

print(' '.join(map(str, ans)))
