import sys
from collections import defaultdict
from bisect import bisect_left

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

S = sr()
T = sr()
S_set = set(S)
T_set = set(T)
if len(T_set - S_set) > 0:
    print(-1); exit()

#これ以降は必ず部分列が出来る
dict_S = defaultdict(list)
for i, s in enumerate(S):
    dict_S[s].append(i)

cur = -1
lenS = len(S)
answer = 0
for t in T:
    cur += 1
    answer += 1
    L = dict_S[t]
    i = bisect_left(L, cur)
    if i == len(L):
        answer += lenS - cur + L[0]
        cur = L[0]
    else:
        answer += L[i] - cur
        cur = L[i]

print(answer)
# 07
