while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        for i, _ in enumerate(range(a)):
            if i == 0 or i == (a - 1):
                x = '#' * b
                print(x)
            else:
                print('#' + '.' * (b - 2) + '#')
        print()
