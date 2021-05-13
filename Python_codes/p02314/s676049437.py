import copy

N, M = map(int, input().split())
c = [0]
c += list(map(int, input().split()))
memo = [N] * (N+1)
flag = [False] * (N+1)
flag[0] = True
memo[0] = 0

for i in range(1, N+1):
    if not flag[i]:
        flag[i] = True
        for j in range(1, M+1):
            if i >= c[j]:
                memo[i] = min(memo[i], memo[i-c[j]] + 1)

print(memo[N])

