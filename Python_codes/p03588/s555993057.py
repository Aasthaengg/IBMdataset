def resolve():
    n = int(input())
    size = 0
    num = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > size:
            size = a
            num = b
    print(size + num)
resolve()