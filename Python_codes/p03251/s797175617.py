def resolve():
    N, M, X, Y = list(map(int, input().split()))
    XN = list(map(int, input().split()))+[X]
    YM = list(map(int, input().split()))+[Y]
    xright = sorted(XN)[-1]
    yleft = sorted(YM)[0]
    print("No War" if xright < yleft else "War")


if '__main__' == __name__:
    resolve()