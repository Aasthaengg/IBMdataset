def resolve():
    A, B, C, K = list(map(int, input().split()))
    MX = 10 ** 18
    if K % 2 == 0:
        print(A-B)
        return
    else:
        print(B-A)
    return

resolve()