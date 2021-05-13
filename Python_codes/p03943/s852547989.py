def resolve():
    a, b, c = list(map(int, input().split()))
    if ((-a + b + c == 0)
        or (a - b + c == 0)
        or (a + b - c == 0)):
        print("Yes")
    else:
        print("No")

resolve()