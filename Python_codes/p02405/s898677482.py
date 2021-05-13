a,b = [],[]
while True:
    (a,b) = [int(x) for x in input().split()]
    if a == b == 0:
        break
    for x in range(a):
        for y in range(b):
            if (x + y) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()