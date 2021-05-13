s = input()
n = 3
for i in range(2 ** n):
    sign = [False] * n
    for j in range(n):
        if (i >> j) & 1:
            sign[j] = True
    cal = int(s[0])
    for i in range(n):
        if sign[i]:
            cal += int(s[i+1])
        else:
            cal -= int(s[i+1])
    if cal == 7:
        print(s[0], end = '')
        for i in range(n):
            if sign[i]:
                print('+' + s[i+1], end = '')
            else:
                print('-' + s[i+1], end = '')
        print('=7')
        break