
n, y = (int(x) for x in input().split())

_10000, _5000, _1000 = 0, 0, 0

exist = False

for i in range(n + 1):

    # print("10000円札 : {0}枚".format(i))
    
    for j in range(n + 1 - i):

        # print("5000円札 : {0}枚".format(j))

        # print("1000円札 : {0}枚".format(k))

        if (i * 10000) + (j * 5000) + ((n - i - j) * 1000) == y :
                # print("答えを発見!")
                _10000, _5000, _1000 = i, j, n - i - j
                exist = True

        # if i + j + (n - i - j) == n :

        #     # print("合計枚数がN枚")
        #     # print("合計金額 : {0}円".format((i * 10000) + (j * 5000) + (k * 1000)))

        #     if (i * 10000) + (j * 5000) + ((n - i - j) * 1000) == y :
        #         # print("答えを発見!")
        #         _10000, _5000, _1000 = i, j, n - i - j
        #         exist = True

    if exist == True :
        break

if exist == True :
    print("{0} {1} {2}".format(_10000, _5000, _1000))
else :
    print('-1 -1 -1')





                

