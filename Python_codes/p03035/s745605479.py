def resolve():
    A, B = map(int, input().split())

    if (A >= 13):
        print(B)
        return
    
    if (6 <= A <= 12):
        print(B // 2)
        return

    print(0)


resolve()