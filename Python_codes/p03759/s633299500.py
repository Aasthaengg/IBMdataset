# A - ι⊥l

# 3本の柱が等間隔に並んでいる
# 柱の高さは左から順に a[m] b[m] c[m]
# 柱の先端が同一線上に並んでいるとき
# ⇔ b - a = c - b
# 美しいな！

# a b c を標準入力から得る
a, b, c = map(int, input().split(maxsplit=3))
# print(a, b, c)

# b - a を計算
pillar_ba = b - a
# c - b を計算
pillar_cb = c - b
# print(pillar_ba, pillar_cb)

# pillar_ba ⇔ pillar_cb の時　Yes
# そうでないとき　No を代入
if pillar_ba == pillar_cb:
    answer = "YES"
else:
    answer = "NO"

# 結果を出力
print(answer)
