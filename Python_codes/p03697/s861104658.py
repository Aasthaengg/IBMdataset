# A - Restricted

# 二つの整数 A B を入力
# A + B を出力
# A + B >= 10 の時 error と出力

# A B を標準入力から得る
A, B = map(int, input().split())
# print(A, B)

# A + B < 10 の時 A + B を代入
# それ以外は error を代入

if (A + B) < 10:
    answer = A + B
else:
    answer = "error"

# 結果を出力
print(answer)
