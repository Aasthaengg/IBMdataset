def call(n):
    i = 1
    while i <= n:
        if i % 3 == 0:
            print(' %d' % i, end='')
        else:
            x = i
            while x > 0:
                if x % 10 == 3:
                    print(' %d' % i, end='')
                    break
                x = int(x/10)
        i += 1
    print('')

line = input()
n = int(line)

call(n)