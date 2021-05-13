from collections import defaultdict

n = int(input())
S = [input() for i in range(n)]
m = int(input())
T = [input() for i in range(m)]

dictS = defaultdict(int)
dictT = defaultdict(int)

for s in S:
    dictS[s] += 1
for t in T:
    dictT[t] += 1

res = 0
for key in dictS:
    res = max(res, dictS[key] - dictT[key])
print(res)
