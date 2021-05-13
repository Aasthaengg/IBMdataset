# AGC 20 A
n, a, b = [int(el) for el in input().split(' ')]

while 1 <= a <= n and 1 <= b <= n:
    if b != a + 1 and 1 <= a +1 <= n:
        a = a + 1
    elif b != a - 1 and 1 <= a - 1 <= n:
        a = a - 1
    else:
        print('Borys')
        break
    if a != b - 1 and 1 <= b - 1 <= n:
        b = b - 1
    elif a != b + 1 and 1 <= b + 1 <= n:
        b = b + 1
    else:
        print('Alice')
        break

