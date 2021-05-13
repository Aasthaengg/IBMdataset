# A - Between Two Integers

# A B C の3つの整数が与えられる
#  整数 C が　A以上　かつ　B以下である時　Yes
# そうでないとき　No

# A B C を標準入力から得る
A, B, C = map(int, input().split(maxsplit=3))

if A <= C <= B:
    answer = "Yes"
else:
    answer = "No"

# 結果を出力
print(answer)
