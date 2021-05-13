from collections import Counter

# input
N = int(input())
S = Counter([input() for i in range(N)])
M = int(input())
T = Counter([input() for j in range(M)])

# check
max_cnt = 0
for s in S.keys():
    cnt = S[s]
    if s in T.keys():
        cnt -= T[s]

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
