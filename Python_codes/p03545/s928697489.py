num = input()

for bit in range(2**3):
    op = ["+", "+", "+"]
    for i in range(3):
        if (bit >> i) & 1:
            op[i] = "-"
    if eval(num[0]+op[0]+num[1]+op[1]+num[2]+op[2]+num[3]) == 7:
        print("{}=7".format(num[0]+op[0]+num[1]+op[1]+num[2]+op[2]+num[3]))
        break
