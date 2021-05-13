from sys import stdin
input = stdin.readline

N = 100
WHITE = 0 # 未訪問
GRAY = 1 # 訪問したが、スタックに残っている
BLACK = 2 # 訪問完了済み

M = [[0]*N for _ in range(N)] # n*nの隣接行列の作成
color = [WHITE]*N  # colorの初期化
d = [0]*N # 最初の訪問時刻のタイムスタンプ
f = [0]*N # 完了時刻のタイムスタンプ

def dfs_visit(u): # uの訪問処理
    global tt
    color[u] = GRAY
    tt += 1
    d[u] = tt # 最初の訪問
    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE: # 深さがあれば再帰的に処理をする
            dfs_visit(v)
    color[u] = BLACK # uに関する全ての深さを探索しきった処理
    tt += 1
    f[u] = tt # 訪問の完了

def dfs():
    global tt
    tt = 0

    for u in range(n):
        if color[u] == WHITE: # 未訪問のuを始点にする
            dfs_visit(u)
    for u in range(n): # 最終的な表示処理
        print(str(u+1) + ' ' + str(d[u]) + ' ' + str(f[u]))

n = int(input())
for _ in range(n): # 隣接行列の作成
    u, k, *vv = input().split()
    u = int(u)-1  # 0オリジンにする
    k = int(k)    # kは使わない
    for v in vv:
        v = int(v)-1
        M[u][v] = 1
dfs()

