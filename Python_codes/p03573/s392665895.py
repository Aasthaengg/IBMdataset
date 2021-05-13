# A - One out of Three

# A B C は整数
# 上記2つは同じ整数で　1つだけ異なる整数
# ex) A = 5,B = 7,C = 5  ...  A ⇔ C Bは異なる値
# 3つの整数のうち 1つのことなる整数を出力させる

# A B C を標準入力
A, B, C = map(int, input().split(maxsplit=3))
# print(A, B, C)

# 以下で条件を分けて代入。
# 1. A ⇔ B の時 C を代入。
# 2. A ⇔ C の時 B を代入。
# 3. B ⇔ C の時 A を代入。

if A == B:
    answer = C
elif A == C:
    answer = B
else:
    answer = A

# 結果を出力
print(answer)
