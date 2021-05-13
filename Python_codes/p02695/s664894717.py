N, M, Q = map(int, input().split())
lis = []
for i in range(Q):
    a = list(map(int, input().split()))
    lis.append(a)


big_lis = []


def dfs(string, n, m):
    if n == (N - 1):
        for i in range(m, M + 1):
            big_lis.append(string + [i])
    else:
        for i in range(m, M + 1):
            dfs(string + [i], n + 1, i)


dfs([], 0, 1)

MAX_A = 0
for small_lis in big_lis:
    D = 0
    for j in range(Q):
        if small_lis[int(lis[j][1]) - 1] - small_lis[int(lis[j][0]) - 1] == int(lis[j][2]):
            D += int(lis[j][3])
    MAX_A = max(MAX_A, D)
print(MAX_A)
