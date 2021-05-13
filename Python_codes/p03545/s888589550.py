ABCD = list(input())

for i in range(2 ** 3):
    ptn = ['-'] * 3
    for j in range(3):
        if (i >> j) & 1:
            ptn[len(ptn) - j - 1] = '+'

    formula = ''.join([n + op for n, op in zip(ABCD, ptn + [''])])
    if eval(formula) == 7:
        print(formula + '=7')
        exit()
