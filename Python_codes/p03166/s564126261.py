#%%
from sys import stdin, setrecursionlimit as srl
from threading import stack_size
srl(int(1e9)+7)
stack_size(int(1e8))

def func(x, graph, flag, dp):
    if (flag[x]):
        return dp[x]

    flag[x] = 1
    check = 0
    for i in graph[x]:
        check = max(check, func(i, graph, flag, dp) + 1)

    dp[x] = check

    return dp[x]

N, M = [int(i) for i in input().split()]
flag = [0] * (N + 1)
dp = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
#%%
for _ in range(M):
    temp_x, temp_y = [int(i) for i in input().split()]
    graph[temp_x].append(temp_y)

#%%
ans = 0
for i in range(1, N + 1):
    ans = max(ans, func(i, graph, flag, dp))

print(ans)
