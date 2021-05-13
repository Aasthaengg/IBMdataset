import numpy as np

N, K = map(int, input().split())
S = np.array(list(input()))
S = (S == 'L') * 1
inner01 = 0
outer10 = 0
happy = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        happy += 1
    elif S[i] - S[i + 1] == 1:
        outer10 += 1
    else:
        inner01 += 1
up = min(inner01, min(K, outer10))
happy += 2 * up
if K - up >= 1 and outer10 - up >= 1 and S[0] == 1:
    happy += 1
if K - up >= 2 and outer10 - up >= 2 and S[-1] == 0:
    happy += 1
if K - up >= 1 and inner01 - up >= 1 and S[0] == 0:
    happy += 1
if K - up >= 2 and inner01 - up >= 2 and S[-1] == 1:
    happy += 1
print(happy)