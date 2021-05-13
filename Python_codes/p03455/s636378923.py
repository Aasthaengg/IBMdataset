# A - Product
# 2つの整数 a × b が偶数か奇数かを判定する。

# 整数 a b の入力
a, b = map(int, input().split())
# print(a, b)

# a × b　を value に代入
value = a * b
# print(value)

# value が 奇数 か 偶数 かを判定する
if value % 2 == 0:
    # print('guusuu')
    answer = 'Even'
else:
    # print('kisuu')
    answer = 'Odd'

# 結果の表示
print(answer)
