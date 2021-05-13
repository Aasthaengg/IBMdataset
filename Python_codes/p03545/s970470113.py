n = [int(x) for x in input()]
for i in range(2 ** 3):
    a = list([str(n[0]), '-', str(n[1]), '-', str(n[2]), '-', str(n[3])])
    total = n[0]
    for j in range(3):
        if ((i >> j) & 1):
            a[int(2*j)+1] = '+'
            total = total + n[j+1]
        else:
            total = total - n[j+1]
    if total == 7:
        a.append('=7')
        print(''.join(a))
        exit()