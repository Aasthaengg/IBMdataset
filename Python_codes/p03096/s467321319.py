from collections import defaultdict
N = int(input())
C = [int(input()) for _ in range(N)]
dic = defaultdict(list)
for i in range(N):
    dic[C[i]].append(i)
es = [[] for _ in range(N)]
for i in range(N - 1):
    es[i].append(i + 1)
for key in dic:
    if len(dic[key]) == 1:
        continue
    i, L, v1, v2 = 1, len(dic[key]) - 1, dic[key][0], dic[key][1]
    while True:
        if v1 + 1 != v2:
            es[v1].append(v2)
        v1 = v2
        if i < L:
            i += 1
            v2 = dic[key][i]
        else:
            break
dp = [0 for _ in range(N)]
dp[0], MOD = 1, 10**9 + 7
for i in range(N - 1):
    for j in es[i]:
        dp[j] = (dp[j] + dp[i]) % MOD
print(dp[N - 1])