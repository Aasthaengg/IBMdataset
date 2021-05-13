a_num_str, operator, b_num_str = map(str, input().split())

a_num_int = int(a_num_str)
b_num_int = int(b_num_str)

if operator == "+" :
    sum_a_b = a_num_int + b_num_int
    print(sum_a_b)
elif operator == "-" :
    sum_a_b = a_num_int - b_num_int
    print(sum_a_b)