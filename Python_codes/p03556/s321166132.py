def resolve():
    n = int(input())
    for i in range(n, 0, -1):
        if (i**0.5)%1 == 0:
            print(i)
            break
resolve()