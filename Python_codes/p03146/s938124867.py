s = int(input())
l = [s]

a = s
for i in range(2, 10**6):
    if a % 2 == 0:
        if a // 2 in l:
            print(i)
            exit()
        l.append(a // 2)
        a = a // 2
    else:
        if 3 * a + 1 in l:
            print(i)
            exit()
        l.append(3 * a + 1)
        a = 3 * a + 1
