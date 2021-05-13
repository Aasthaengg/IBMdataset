def myfunc(op):
    if op == 1:
        return "+"
    else:
        return "-"


a, b, c, d = [int(i) for i in list(input())]

for k in [0, 1]:
    for j in [0, 1]:
        for i in [0, 1]:
            op = [-1, -1, -1]
            if k == 0:
                op[0] = 1
            if j == 0:
                op[1] = 1
            if i == 0:
                op[2] = 1
            if a + b * op[0] + c * op[1] + d * op[2] == 7:
                x = myfunc(op[0])
                y = myfunc(op[1])
                z = myfunc(op[2])
                print(f"{a}{x}{b}{y}{c}{z}{d}=7")
                exit()