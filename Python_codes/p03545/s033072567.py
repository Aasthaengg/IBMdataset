n = [int(x) for x in input()]
op_cnt = len(n) - 1
for i in range(1 << op_cnt):
    op = ['-'] * op_cnt
    for j in range(op_cnt):
        if (i >> j) & 1:
            op[op_cnt - 1 - j] = '+'
    formula = "{}{}{}{}{}{}{}".format(n[0], op[0], n[1], op[1], n[2], op[2], n[3])
    if eval(formula) == 7:
        print(formula + '=7')
        break
