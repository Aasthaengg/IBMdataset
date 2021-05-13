def resolve():
    A, B = map(int, input().split())
    print(A+B if A+B<=9 else "error")
resolve()