# A - HonestOrDishonest

# 正直者は常にほんとうのことを言い、嘘つきは常に嘘を言います

#  文字 a  と  b  が入力として与えられます。
#  これらはそれぞれ H か D のどちらかです

# すべて AtCoDeer君の発言
# a = H or D    私が H or D
# b = H or D    TopCoDeer 君が H or D

# TopCoDeer が　正直者なら H 嘘つきなら D を出力

# 文字列 a b を標準入力から得る
a, b = map(str, input().split())
# print(a, b)

# a ⇔ H の時、 b を代入
# そうでなく、 b ⇔ H の時、 D を代入
# 上記以外の場合、 H を代入

if a == "H":
    answer = b
elif b == "H":
    answer = "D"
else:
    answer = "H"

# 結果を出力
print(answer)
