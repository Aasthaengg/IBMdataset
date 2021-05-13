
def resolve():
    X, A, B = list(map(int, input().split()))
    if B <= A:
        print("delicious")
    elif B <= A+X:
        print("safe")
    else:
        print("dangerous")


if '__main__' == __name__:
    resolve()