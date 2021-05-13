nums = input()

op_cnt = len(nums) -1

sum = 0

for i in range(2 ** op_cnt):
    op = [""] * op_cnt
    for j in range(op_cnt):
        if(i >> j & 1):
            op[j] = "+"
    # print(op)

    formula = ""

    for p_n,p_o in zip(nums,op + [""]):
        formula += (p_n + p_o)

    sum += eval(formula)

print(sum)