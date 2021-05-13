N,K = map(int,input().split())
inc = abs(N-K)

if N <= inc :
    print(N)
elif K/2 < N%K :
    print(K-N%K)
else :
    print(N%K)