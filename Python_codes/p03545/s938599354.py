abcd_origin = list(input())

for i in range(8):
    abcd = abcd_origin.copy()
    temp = []
    temp.append(abcd.pop(0))
    for j in range(3):
        if (i >> j) & 1:
            temp.append('+')
            temp.append(abcd.pop(0))
        else:
            temp.append('-')
            temp.append(abcd.pop(0))

    result = int(temp[0])

    for k in range(3):
        if temp[2 * k + 1] == '+':
            result += int(temp[2 * k + 2])
        else:
            result -= int(temp[2 * k + 2])

    if result == 7:
        equ = ''.join(temp) + '=7'
        print(equ)
        exit()
