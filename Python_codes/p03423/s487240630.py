def resolve():
    n = int(input())
    c = 0
    while n - 3 >= 0:
        n -= 3
        c += 1
    print(c)
resolve()