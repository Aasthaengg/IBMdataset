def combinations(N, K):
    N = int(N)
    K = int(K)
    if N == K:
        return 1
    else:
        return N - K + 1
    
N, K = input().split(' ')

print(combinations(N, K))