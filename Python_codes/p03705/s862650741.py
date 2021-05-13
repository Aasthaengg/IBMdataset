n, a, b = [int(i) for i in input().split()]
c = b * (n - 1) + a
d = a * (n - 1) + b

if a > b:
    print(0)
elif n == 1:
    if a != b:
        print(0)
    else:
        print(1)
else:
    print(c-d+1)
