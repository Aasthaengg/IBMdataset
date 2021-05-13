i = int(input())

for j in range(1, i + 1) :
    tmpJ = int(j // 10)
    isFinish = False

    if j % 3 == 0 :
        print(' {}'.format(j), end = '')
    elif (j % 10 == 3) :
        print(' {}'.format(j), end = '')
    elif tmpJ % 10 == 3 :
        print(' {}'.format(j), end = '')
    elif tmpJ != 0 :
        tmpJ //= 10
        while tmpJ != 0 and (not isFinish) :
            if tmpJ % 10 == 3 :
                print(' {}'.format(j), end = '')
                isFinish = True
            tmpJ //= 10
print()