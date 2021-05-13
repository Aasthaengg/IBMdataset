import numpy as np
N, K = map(int,input().split())
S = input()
L = np.zeros(N+1, int)
flag = '1'
i = 0
for char in S:
    if char == flag:
        L[i] += 1
    else:
        i += 1
        flag = char
        L[i] += 1

W = min(2 * K + 1, N + 1)

ans = L[:W].sum()

cnt = L[:W].sum()

for i in range((N+1-W) // 2):
    cnt = cnt - L[i*2] - L[i*2+1] + L[i*2+W] + L[i*2+W+1]
    ans = max(ans, cnt)
print(ans)