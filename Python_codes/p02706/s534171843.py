def resolve():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(-1 if sum(A)>N else N-sum(A))



if '__main__' == __name__:
    resolve()