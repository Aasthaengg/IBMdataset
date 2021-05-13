N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
S = K
for K in range(K,N):
    if A[K-S] < A[K]:
        print("Yes")
    else :
        print("No")