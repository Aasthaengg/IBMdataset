import sys
sys.setrecursionlimit(10**7)
N, K = map(int, input().split())

e = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

col = [-1 for i in range(N)]
col[0] = 0
MOD = 10 ** 9 + 7


def dfs(i, ans, depth):

    if depth == 1:
        num = K - 1
    else:
        num = K - 2
    for v in e[i]:
        if col[v] == -1:
            col[v] = 0
            ans = (ans * num) % MOD
            num -= 1
            ans = dfs(v, ans, depth+1)

    return ans


print(dfs(0, K, 1))
