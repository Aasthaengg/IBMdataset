def resolve():
    N, K = list(map(int, input().split()))
    H = sorted(list(map(int, input().split())))
    print(0 if N<=K else sum(H[:N-K]))

if '__main__' == __name__:
    resolve()