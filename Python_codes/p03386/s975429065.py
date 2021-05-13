def resolve():
    A, B, K = map(int, input().split())
    if 2*K > B-A+1:
        for _ in range(B-A+1):
            print(A+_)
    else:
        for i in range(K):
            print(A+i)
        for j in range(K):
            print(B-K+j+1)
resolve()