a, b, c, d = input()
op = ["+", "-"]

for op1 in op:
    for op2 in op:
        for op3 in op:
            check = a + op1 + b + op2 + c + op3 + d
            if eval(check) == 7:
                print(check + "=7")
                exit()