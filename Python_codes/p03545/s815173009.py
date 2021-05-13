n = input()
op_cnt = len(n) - 1  
for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt  
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"  

    formula = ""*(2+len(n)-1)
    formula+=n[0]
    for w in range(len(n)-1):
        formula+=op[w]+n[w+1]
    if eval(formula) == 7:
        print(formula + "=7")
        break