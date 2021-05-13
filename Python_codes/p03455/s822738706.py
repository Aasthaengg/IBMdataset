
# 入力
a, b = map(int, input().split())

# 処理
product = a * b

# 出力
if product % 2 == 0:
    print('Even')
elif product % 2 == 1:
    print('Odd')
else:
    print('Error')