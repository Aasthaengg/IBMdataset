# AGC207A

def f(n, a, b):
    if (b - a) % 2:
        print('Borys')
    else:
        print('Alice')

n, a, b = map(int, input().split())
#f(5, 2, 4)
#f(2, 1, 2)
#f(58, 23, 42)
f(n, a, b)
