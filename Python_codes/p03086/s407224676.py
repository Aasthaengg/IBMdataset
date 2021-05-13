# author:  Taichicchi
# created: 09.09.2020 23:22:31

import sys

S = input()
N = len(S)
ans = 0
for i in range(N):
    for j in range(i, N):
        if all('ACGT'.count(c) == 1 for c in S[i : j + 1]):
            ans = max(ans, j - i + 1)
print(ans)
