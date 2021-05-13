N,K = map(int,input().split())
A = [int(x) for x in input().split()]
for i in range(K,N):
    if A[i] > A[i-K]:
        print('Yes')
    else:
        print('No')