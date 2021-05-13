def f_10_to_m2(n):
    if n == 0:
        return 0 

    digits = []
    i = 0
    base = 1
    while n != 0:
        if n % (base*2) == 0:
            digits.append(0)
        else:
            digits.append(1)
            n -= base
        i += 1
        base *= -2
    return ''.join(map(str, reversed(digits)))

print(f_10_to_m2(int(input())))