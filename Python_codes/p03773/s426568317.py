
def resolve():
    A, B = list(map( int, input().split() ))
    print(A+B if A+B < 24 else A+B-24)


if '__main__' == __name__:
    resolve()