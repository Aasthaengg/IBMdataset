n, i = int(input()), 1
while True:
    x = i
    if x%3 == 0:
        print(" %d" %(i), end='')
    else:
        while True:
            if x%10 == 3:
                print(" %d" % (i), end='')
                break
            x //= 10
            if x == 0:
                break
    i += 1
    if i > n:
        break
print()