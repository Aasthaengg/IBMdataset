while True:
    A, B, C = map(str, input().split())
    a = int(A)
    b = int(C)
    if B=="?":
        break
    elif B=="+":
        print(a+b)
    elif B==("-"):
        print(a-b)
    elif B=="*":
        print(a*b)
    elif B==("/"):
        print(a//b)