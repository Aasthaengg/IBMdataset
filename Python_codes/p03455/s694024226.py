# 標準入力から整数 a, b を取得する
a, b = map(int, input().split())

# a と b の積が奇数か否かを判定し、結果を出力する
input_product_num = a * b

result = 'Odd'
if (input_product_num % 2) == 0:
    result = 'Even'

print(result)