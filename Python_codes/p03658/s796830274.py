def resolve():
    N, K = list(map(int, input().split()))
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    print(sum(L[:K]))


if '__main__' == __name__:
    resolve()