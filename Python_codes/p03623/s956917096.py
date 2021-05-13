
def resolve():
    X, a, b = list(map(int, input().split()))
    print("A" if abs(X-a) < abs(X-b) else "B")


if '__main__' == __name__:
    resolve()