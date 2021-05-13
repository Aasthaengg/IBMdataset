A, B, C, D = input()
op = ["+", "-"]

for i in op:
    for j in op:
        for k in op:
            ans = A + i + B + j + C + k + D
            if eval(ans) == 7:
                print(ans + "=7")
                exit()
