import sys
sys.setrecursionlimit(1000000)


def dfs_f(now, kyori):
    kyori_f[now] = kyori
    # 今いる頂点から行ける頂点を順に next に入れてループ
    for next in g[now]:
        # 行ったことがない、白く塗られていない
        if not memo_f[next] and next != n - 1:
            memo_f[next] = True
            dfs_f(next, kyori + 1)


def dfs_s(now, kyori):
    kyori_s[now] = kyori
    # 今いる頂点から行ける頂点を順に next に入れてループ
    for next in g[now]:
        # 行ったことがない、黒く塗られていない
        if not memo_s[next] and next != 0:
            memo_s[next] = True
            dfs_s(next, kyori + 1)


n = int(input())
g = [[] * n for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# フェネック
memo_f = [False for i in range(n)]  # 訪れたことがあるか
kyori_f = [float("inf") for i in range(n)]  # 始点からの距離
memo_f[0] = True
dfs_f(0, 0)

# すぬけ
memo_s = [False for i in range(n)]  # 訪れたことがあるか
kyori_s = [float("inf") for i in range(n)]  # 始点からの距離
memo_s[n - 1] = True
dfs_s(n - 1, 0)

black = 0
white = 0
for i in range(n):
    if kyori_f[i] <= kyori_s[i]:
        black += 1
    else:
        white += 1

if black > white:
    print("Fennec")
else:
    print("Snuke")