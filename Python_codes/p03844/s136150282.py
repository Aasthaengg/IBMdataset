# A - Addition and Subtraction Easy


# A op B という式の値を計算したい
# op ⇔ + or -

# A op B とstr型で標準入力する
A, op, B = map(str, input().split(maxsplit=3))
# print(A, op, B)

# A B を int型 に変換
A = int(A)
B = int(B)

# op が　+ の場合 A + B
# それ以外の時は   A -B

if op == "+":
    answer = A + B
else:
    answer = A - B

# 結果を出力
print(answer)
