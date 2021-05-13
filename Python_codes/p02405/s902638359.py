# coding: utf-8

list = []

while True:
    num = input().rstrip().split(" ")
    if (int(num[0]) == 0) and (int(num[1]) == 0):
        break
    list.append(num)

for i in range(len(list)):
    for j in range(int(list[i][0])):
        for k in range(int(list[i][1])):
            if ((j % 2) == 0):
                if ((k % 2) == 0):
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if ((k % 2) == 0):
                    print(".", end="")
                else:
                    print("#", end="")
        print()
    print()