def myfunc(op):
    if op:
        return "+"
    else:
        return "-"


a, b, c, d = [int(i) for i in list(input())]

for j in range(8):
    op = [[1, "+"]] * 3
    for i in range(3):
        if (j >> i) & 1:
            op[i] = [-1, "-"]
    if a + b * op[0][0] + c * op[1][0] + d * op[2][0] == 7:
        print(f"{a}{op[0][1]}{b}{op[1][1]}{c}{op[2][1]}{d}=7")
        exit()