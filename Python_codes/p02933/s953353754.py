# 整数 a と、英小文字からなる文字列 s が入力されます。
# a が 3200以上なら s と出力し、a が 3200 未満なら red と出力するプログラムを書いてください。

# 標準入力から 整数a と文字列s を取得する
input_a = int(input())
input_s = input()

# a が3200以上／3200未満 なのかを判定する
# # output_s = 'Error: Input Value is OutOfRange. Sorry!'
# # if (input_a <= 2800) or (input_a >= 5000):
# #     output_s = output_s
# else:

output_s = 'pink'
if input_a >= 3200:
    output_s = input_s
elif input_a < 3200:
    output_s = 'red'

# 結果を出力する
print(output_s)
