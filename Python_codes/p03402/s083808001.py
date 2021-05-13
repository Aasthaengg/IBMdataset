def print_component(a, b, n):
    for _ in range(25):
        print(a * 100)
        if n:
            x = min(n, 50)
            n -= x
            print((a+b)*x + a*2*(50-x))
        else:
            print(a * 100)


A, B = map(int, input().split())

print('100 100')
print_component('#', '.', A - 1)
print_component('.', '#', B - 1)
