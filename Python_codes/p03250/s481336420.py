def resolve():
    A, B, C = list(map(int, input().split()))
    print(max([10*A+B+C, 10*B+C+A, 10*C+A+B]))


if '__main__' == __name__:
    resolve()