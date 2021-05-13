k = int(input())

if k < 50:
    print(2)
    if k % 2 == 0:
        print(str(1 + k // 2) + ' ' + str(1 + k // 2))
    else:
        print(str(k // 2) + ' ' + str(3 + k // 2))
else:
    print(50)
    a = k // 50 + 49
    if k % 50 == 0:
        l = [str(a)] * 50
        print(' '.join(l))
    else:
        alpha = k % 50
        l = [str(a + 51 - alpha)] * alpha + [str(a - alpha)] * (50 - alpha)
        print(' '.join(l))