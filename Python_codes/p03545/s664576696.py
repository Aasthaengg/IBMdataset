num = input()

ls = [0] * 3
for i in range(2 ** 3):
    make7 = int(num[0])
    for j in range(3):
        if (i >> j) & 1:
            make7 += int(num[j+1])
            ls[j] = "+"
        else:
            make7 -= int(num[j+1])
            ls[j] = "-"
    if make7 == 7:
        print(num[0] + ls[0] + num[1] + ls[1] + num[2] + ls[2] + num[3] + "=7")
        exit()
