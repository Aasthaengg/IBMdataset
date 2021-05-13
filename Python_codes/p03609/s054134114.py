
def resolve():
    X, t = list(map(int, input().split()))
    print(max(0, X - t))


if '__main__' == __name__:
    resolve()