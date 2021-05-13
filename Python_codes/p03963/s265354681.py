def resolve():
    N, K = list(map(int, input().split()))
    print(K*((K-1)**(N-1)))

if '__main__' == __name__:
    resolve()