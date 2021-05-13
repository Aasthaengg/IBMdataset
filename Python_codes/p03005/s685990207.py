def resolve():
    A, B = map(int, input().split())
    print("0" if B == 1 else A-B)
resolve()