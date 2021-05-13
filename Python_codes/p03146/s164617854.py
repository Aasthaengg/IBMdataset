s = int(input())
li = []
a = s
for i in range(1, 10 ** 6 + 1):
    if i == 1:
        a = s
    else:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
    if a in li:
        print(i)
        exit()
    li.append(a)
