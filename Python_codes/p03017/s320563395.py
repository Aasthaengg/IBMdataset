#58 A - Kenken Race
import sys
sys.setrecursionlimit(10**7)
N,A,B,C,D = map(int,input().split())
S = input()
A,B,C,D = A-1,B-1,C-1,D-1

# A が B を抜かせるエリア
if B == 1:
    a = S.find('...') + 1
else:
    a = S.find('...',3) + 1

dx = [1,2]

# 先に移動させる方の関数
def dfs_ini(v,seen_ini,X):
    seen_ini[v] = True# v を訪問済みにする
    for i in range(2):
        next_v = v + dx[i]
        # next_v が範囲外 or 壁の場合 or 他方が存在する場合
        if not(-1<next_v<N):
            continue
        if (S[next_v] == '#') or (next_v == X):
            continue
        if seen_ini[next_v] == True:# next_v が探索済みならスルー
            continue
        dfs_ini(next_v,seen_ini,X)

# 後に移動させる方の関数
def dfs_fin(w,seen_fin,Y):
    seen_fin[w] = True# w を訪問済みにする
    for j in range(2):
        next_w = w + dx[j]
        # next_w が範囲外 or 壁の場合 or 他方が存在する場合
        if not(-1<next_w<N):
             continue
        if (S[next_w] == '#')  or (next_w == Y):
             continue
        if seen_fin[next_w] == True:# next_w が探索済みならスルー
             continue
        dfs_fin(next_w,seen_fin,Y)

# A を先に動かした方がいいとき
# B を 先に a まで移動させる
if C>D:
    seen_ini_A = [False]*N
    seen_fin_B = [False]*N
    # B を抜かせるエリアがないとき、B の位置はスタート位置
    if (a < B) or (a > D):
        a = B
    dfs_ini(A,seen_ini_A,a)
    dfs_fin(B,seen_fin_B,C)
    result = 'No'
    if seen_ini_A[C] and seen_fin_B[D]:
        result = 'Yes'

# B を先に動かした方がいいとき
else:
    seen_ini_B = [False]*N
    seen_fin_A = [False]*N
    dfs_ini(B,seen_ini_B,A)
    dfs_fin(A,seen_fin_A,D)
    result = 'No'
    if seen_ini_B[D] and seen_fin_A[C]:
        result = 'Yes'

print(result)