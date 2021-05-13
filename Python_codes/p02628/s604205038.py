def resolve():
    N, K = list(map(int, input().split()))
    P = sorted(list(map(int, input().split())))
    print(sum(P[:K]))

if '__main__' == __name__:
    resolve()