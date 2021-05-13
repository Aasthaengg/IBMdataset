N = int(input())
a = [int(i) for i in input().split()]
list = {}
list[8] = 0

for i in a:
    if 1 <= i <= 399:
        list[0] = 1
    elif 400 <= i <= 799:
        list[1] = 1
    elif 800 <= i <= 1199:
        list[2] = 1
    elif 1200 <= i <= 1599:
        list[3] = 1
    elif 1600 <= i <= 1999:
        list[4] = 1
    elif 2000 <= i <= 2399:
        list[5] = 1
    elif 2400 <= i <= 2799:
        list[6] = 1
    elif 2800 <= i <= 3199:
        list[7] = 1
    else:
        list[8] += 1

if len(list) == 1:
    min = 1
else:
    min = len(list) - 1

if list[8] > 0:
    max = len(list) + list[8] - 1
else:
    max = len(list) - 1

print(min,max)
