# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b
# B - fLIP

# ボタンを押す順番と最後のマスの結果は関係ない
# あるボタンを2回押すと0回押した状態になる
# どの行、列のボタンを押しても黒マスの数は同じ
# 行のボタン、列のボタンを何回押したか見る

# 行のボタンをr回、列のボタンをc回押したとき、黒マスの数は
# r*M + c*N - 2*r*c


# N,M <= 1000 だし全探索

n, m, k = map(int, input().split())

can = False


def func(r, c):
    return r * m + c * n - 2 * r * c


for r in range(n + 1):
    for c in range(m + 1):
        can |= func(r, c) == k

print("Yes" if can else "No")
