# A - キャンディーと2人の子供

# 2人の子供がキャンディーの取り合いをしている
# 3個のキャンデーパックがあり、れぞれのパックには
# キャンディーが  a ,  b ,  c  個入っています

# 先生が、上記3個のパックをキャンディーの個数が等しくなるように
# 2人に分けようとしている

# そのような分け方が可能かどうかを判定する。
# 可能なら Yes  そうでないなら No

# a b c を標準入力から得る
a, b, c = map(int, input().split(maxsplit=3))
# print(a, b, c)

# 以下条件で等しく分けることが可能
# a = b + c
# b = a + c
# c = a + b

if a == (b + c):
    answer = "Yes"
elif b == (a + c):
    answer = "Yes"
elif c == (a + b):
    answer = "Yes"
else:
    answer = "No"

# 結果を出力
print(answer)
