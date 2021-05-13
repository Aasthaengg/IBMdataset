
def resolve():
    a, b, c = list(map(int, input().split()))
    print(min(a+b, b+c, c+a))


if '__main__' == __name__:
    resolve()