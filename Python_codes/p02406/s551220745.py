n = input()
s = ''
i = 1
while True:
    x = i
    if (x % 3 == 0):
        s = s + ' ' + str(i)
    else:
        while True:
            if (x % 10 == 3):
                s = s + ' ' + str(i)
                break
            x = int(x / 10)
            if x == 0:
                break
    i = i + 1
    if (i > n):
        break
print s