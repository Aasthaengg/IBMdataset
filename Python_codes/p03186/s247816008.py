def resolve():
    A, B, C = map(int, input().split())
    if A+B+1 >= C:
        print(B+C)
    else:
        print(A+B+B+1)
resolve()