n = int(input())
x = ''
while n != 0:
    if n % (-2) == 0:
        n //= (-2)
        x = '0' + x
    else:
        n = (n - 1) // (-2)
        x = '1' + x
print(x if x else 0)