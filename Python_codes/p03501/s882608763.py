
def resolve():
    N, A, B = list(map(int, input().split()))
    print(B if N * A > B else N * A)


if '__main__' == __name__:
    resolve()