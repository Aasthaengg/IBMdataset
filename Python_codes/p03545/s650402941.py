s = input()
a = [int(x) for x in s]
for bit in range(1 << 3):
    tmp = a[0]
    tmps = str(a[0])

    for i in range(3):
        if bit >> i & 1:
            tmp += a[i + 1]
            tmps += '+' + str(a[i + 1])
        else:
            tmp -= a[i + 1]
            tmps += '-' + str(a[i + 1])
    if tmp == 7:
        print(tmps + '=7')
        exit()
