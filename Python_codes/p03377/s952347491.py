line = input()

a, b, c = [int(n) for n in line.split()]

if c <= a+b and c >= a:
    print('YES')
else:
    print('NO')