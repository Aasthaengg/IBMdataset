x, k, d = [int(x) for x in input().split(' ')]
x = abs(x)

q = x // d
r = x % d

if k >= q:
    if k%2 == q%2:
        print(r)
    else:
        print(d - r)
else:
    print(x - d*k)