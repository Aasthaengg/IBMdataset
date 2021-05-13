n = int(input())

if n % 2 == 1:
    print(0)
else:
    res = 0
    m = 10
    while n // m > 0:
        res += n // m
        m *= 5

    print(res)