N,K=map(int,input().split())
*A,=map(int,input().split())

for i in range(0,N-K):
    print('Yes' if 1<A[i+K]/A[i] else 'No')