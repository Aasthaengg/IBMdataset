n = int(input())
i = 1
a = ''
while i <= n:
    x = i
    if x % 3 == 0:
        a += ' ' + str(i)
    elif x % 10 == 3:
        a += ' ' + str(i)
    else:
        x /= 10
        x = int(x)
        while x:
            if x % 10 == 3:
                a += ' ' + str(i)
                break
            x /= 10
            x = int(x)
    i += 1
print(a)
