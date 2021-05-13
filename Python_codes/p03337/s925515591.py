def resolve():
    A, B = list(map(int, input().split(" ")))
    print(max([A+B, A-B, A*B]))

if '__main__' == __name__:
    resolve()