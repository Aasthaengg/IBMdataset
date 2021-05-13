N = int(input())
a = [int(i) for i in input().split()]
check = [0] * 9
maxx = 0
minn = 0

for i in a:
    if 1 <= i <= 399:
        check[0] += 1
    elif 400 <= i <=799:
        check[1] += 1
    elif 800 <= i <= 1199:
        check[2] += 1
    elif 1200 <= i <= 1599:
        check[3] += 1
    elif 1600 <= i <= 1999:
        check[4] += 1
    elif 2000 <= i <= 2399:
        check[5] += 1
    elif 2400 <= i <= 2799:
        check[6] += 1
    elif 2800 <= i <= 3199:
        check[7] += 1
    elif i >= 3200:
        check[8] += 1

for i in range(9):
    if i <= 7 and check[i] >= 1:
        maxx += 1
        minn += 1
    if i == 8:
        maxx += check[8]
        if minn == 0 and check[8] >= 1:
            minn = 1

print(minn, maxx)