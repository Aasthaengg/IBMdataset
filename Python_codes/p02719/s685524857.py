def resolve():
    N, K = list(map(int, input().split()))
    boundleft = N%K
    boundright = K-N%K
    print(min(boundleft, boundright))

if '__main__' == __name__:
    resolve()