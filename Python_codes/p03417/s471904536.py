# N, Mが十分に大きい時
# 頂点: 4
# 端: 6
# それ以外: 9
# ひっくり返る
# はじめ表なので
# 頂点: 4 -> 表
# 端: 6 -> 表
# それ以外: 9 -> 裏
# となる。
# N, Mが小さい時は場合分けする必要がある
# NかMのどちらかだけが1のとき
# 頂点: 2 -> 表
# 端: 3 -> 裏
# それ以外: 3 -> 裏
# NかMのどちらかだけが2のとき
# 頂点: 4 -> 表
# 端: 6 -> 表
# それ以外: 6 -> 表
# NかMのどちらも1のとき
# 頂点: 1 -> 裏
# 端: 1 -> 裏
# それ以外: 1 -> 裏

# 頂点: max(N, 2) * max(M, 2)
# # 端(N>=3): min((N - 1) * (M), 6)

N, M = map(int, input().split())
N, M = max(N, M), min(N, M)
if N >= 3 and M >= 3:
    ans = N * M - (2 * N + 2 * M - 4)
    print(ans)
    exit()

if N >= 3 and M == 2:
    print(0)
    exit()

if N >= 3 and M == 1:
    print(N * M - 2)
    exit()

if N == 2:
    print(0)
    exit()

if N == 1 and M == 1:
    print(1)
    exit()
