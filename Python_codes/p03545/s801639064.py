a, b, c, d = input()
for i in range(2**3):
    ls = ['+','+','+']
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = '-'
    if eval(a + ls[0] + b + ls[1] + c + ls[2] + d) == 7:
        print(a + ls[0] + b + ls[1] + c + ls[2] + d + '=7')
        exit()