import itertools

n, a, b = map(int, input().split())

if n == 1:
    if a == b:
        print(1)
    else:
        print(0)
elif n == 2:
    print(1)
elif n >= 3:
    if a > b:
        print(0)
    else:
        smin = a * n + (b-a)
        smax = b * n - (b-a)
        print(smax-smin+1)