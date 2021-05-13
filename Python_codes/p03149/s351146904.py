# -*- coding: utf-8 -*-

numbers = [int(e) for e in input().split()]

numList = [1, 4, 7, 9]

if numbers[0] in numList:
    numin = numList.index(numbers[0])
    del numList[numin]

    if numbers[1] in numList:
        numin = numList.index(numbers[1])
        del numList[numin]

        if numbers[2] in numList:
            numin = numList.index(numbers[2])
            del numList[numin]

            if numbers[3] in numList:
                numin = numList.index(numbers[3])
                print('YES')

            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')