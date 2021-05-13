n = input()
for i in range(2**3):
    op =[]
    for j in range(3):
        if i >> j & 1:
            op.append('+')
        else:
            op.append('-')
    formula = n[0] + op[0] + n[1] + op[1] + n[2] + op[2] + n[3]
    if eval(formula) == 7:
        print(formula + '=7')
        exit()