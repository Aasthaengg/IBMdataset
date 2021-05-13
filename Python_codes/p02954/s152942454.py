S = input() + 'R'
R = 0
L = 0
ans = [0] * (len(S))
for i in range(len(S)):
    if S[i] == 'R':
        R += 1
        if L > 0:
            ans[i - L] += (L + 1) // 2
            ans[i - L - 1] += L // 2
            L = 0
    elif S[i] == 'L':
        L += 1
        if R > 0:
            ans[i] += R // 2
            ans[i - 1] += (R + 1)// 2
            R = 0
print(*ans[:-1])
