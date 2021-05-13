n = int(input())

if n == 0:
    print(0)
    
else:
    digits = []
    i = 0
    base = 1
    while n != 0:
        if n % (base*2) == 0:
            digits.append('0')
        else:
            digits.append('1')
            n -= base

        i += 1
        base *= -2##

    print(''.join(digits[::-1]))