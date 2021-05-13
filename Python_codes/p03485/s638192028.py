
def resolve():
    A, B = list(map(int, input().split(" ")))
    import math
    print(math.ceil((A+B)/2))


if '__main__' == __name__:
    resolve()