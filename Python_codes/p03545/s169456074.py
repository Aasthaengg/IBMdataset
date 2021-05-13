num = input()

op_count = 3

for i in range(2**op_count):
    op = ["-"] * op_count
    for j in range(op_count):
        if (i >> j & 1):
            op[j] = "+"

    equ = ""

    for n_i,o_i in zip(num,op + [""]):
        equ += n_i + o_i
    if(eval(equ) == 7):
        print(equ + "=7") 
        break
