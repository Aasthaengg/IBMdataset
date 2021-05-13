import numpy as np
N = int(input())
S_1 = input()
S_2 = input()

S = []
S.append([ord(s) for s in S_1])
S.append([ord(s) for s in S_2])
S = np.array(S).T

mod = 10 ** 9 + 7

ans = 1
flag = False

for i in range(N):
    if flag:
        flag = False
        continue
    if S[i][0] == S[i][1]: # 横
        if i == 0:
            ans *= 3
        else:
            if S[i - 1][0] == S[i - 1][1]:
                ans *= 2
    else: # 縦
        if i == 0:
            ans *= 6
        else:
            if S[i - 1][0] == S[i - 1][1]:
                ans *= 2
            else:
                ans *= 3
        flag = True
    ans %= mod

print(ans)