def resolve():
    N, M = list(map(int, input().split()))
    A = 1900*M+100*(N-M)
    print((2**M)*A)


if '__main__' == __name__:
    resolve()