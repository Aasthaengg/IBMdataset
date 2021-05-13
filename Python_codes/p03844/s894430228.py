# 文字で出力する
a_num_str, operator, b_num_str = map(str, input().split())

# a_num_str と b_num_str を 整数にする。
a_num_int = int(a_num_str)
b_num_int = int(b_num_str)

# operator は 「+」「-」の２つがあるので場合わけし計算する。
if operator == '+':
    sum_a_b = a_num_int + b_num_int
    print(sum_a_b)
elif operator == '-':
    sub_a_b = a_num_int - b_num_int
    print(sub_a_b)