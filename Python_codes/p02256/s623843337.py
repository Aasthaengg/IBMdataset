x, y = [int(a) for a in input().split()]

def divisor(x, y):
    while x % y != 0:
        amari = x % y
        if amari == 0:
            return y
        x = y
        y = amari
    return y
print(divisor(x, y))