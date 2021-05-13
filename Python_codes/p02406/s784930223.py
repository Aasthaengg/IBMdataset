n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or i % 10 == 3:
        print(' %d' % i, end='')
    else:
        tmp = i
        while tmp is not 0:
            tmp //= 10
            if tmp % 10 == 3:
                print(' %d' % i, end='')
                break
print()



