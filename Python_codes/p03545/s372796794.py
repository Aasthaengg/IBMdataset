s = input()

for i in range(2**3):
    op = ["+"]*3
    op.append("")
    fomula = ""
    for j in range(3):
        if(i >> j & 1):
            op[j] = "-"
    for k in range(4):
        fomula += s[k] + op[k]
    if eval(fomula) == 7:
        print(fomula + "=7")
        break
