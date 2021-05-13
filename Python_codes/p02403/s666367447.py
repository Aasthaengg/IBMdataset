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
            print("#", end="")
        print()
    print()