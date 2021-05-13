a, b, c, d = input()
op = [0] * 3

for i in range(2 ** 3):
    for j in range(3):
        if (i >> j) & 1 == 1:
            op[j] = '+'
        else:
            op[j] = '-'
    expression = a + op[0] + b + op[1] + c + op[2] + d
    if eval(expression) == 7:
        print(expression+'=7')
        break