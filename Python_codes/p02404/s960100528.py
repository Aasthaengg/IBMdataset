while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    for n in range(a):
        if n == 0 or n == a - 1:
            print("#" * b)
        else:
            print("#" + "." * (b - 2) + "#")
    print("")
