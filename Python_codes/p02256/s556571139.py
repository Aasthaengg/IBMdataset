def converter(a, b):
    if b%a == 0:
        return a
    else:
        return converter(b % a, a)


a, b = sorted([int(x) for x in raw_input().split(' ')])
print converter(a, b) 