S = input()
T = input()

# 例abcdefg...のように文字列が1対1の矢印関係の場合は、
# どのような場合でも置き換えできる。問題は同じ文字が複数現れる場合

# S上に同じ文字sのある場所には
# T上にも同じ文字tがなくてはならない
# つまり、同じ値になっているインデックスの集合を取れば
# 全部同じになっているはず

# 文字種ごとにインデックスの集合を求める
ns = len(S)
indexS = {}
for i in range(ns):
    s = S[i]
    if s in indexS:
        indexS[s].append(i)
    else:
        indexS[s] = [i]
indexT = {}
for i in range(ns):
    t = T[i]
    if t in indexT:
        indexT[t].append(i)
    else:
        indexT[t] = [i]
# 先頭の文字から、インデックスの集合が等しいかチェック
for i in range(ns):
    s = S[i]
    t = T[i]
    i_s = len(indexS[s])
    i_t = len(indexT[t])
    if i_s != i_t:
        print("No")
        break
else:
    print("Yes")
