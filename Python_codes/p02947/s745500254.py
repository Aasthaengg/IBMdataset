from collections import Counter
N = int(input())
S = [[0]*26 for _ in range(N)]
for i in range(N):
    for s in input():
        S[i][ord(s)-ord("a")] += 1
    S[i] = tuple(S[i])
res = 0
for value in Counter(S).values():
    res += value*(value-1)//2

print(res)