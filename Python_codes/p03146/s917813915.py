s = int(input())

l = [s]
temp = s
for i in range(2, 10**7):

    if temp % 2 == 0:
        temp //= 2
    else:
        temp = 3 * temp + 1

    if temp in l:
        print(i)
        exit()
    else:
        l.append(temp)
