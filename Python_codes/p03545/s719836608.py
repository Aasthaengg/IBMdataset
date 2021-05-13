abcd = list(input())
a, b, c, d = abcd
sign = ['+', '-']
for i in range(2**3):
    s = a
    for j in range(3):
        if (i>>j) & 1:
            s += sign[0]
        else:
            s += sign[1]
        s += abcd[j+1]
    if eval(s) == 7:
        print(s + "=7")
        exit()