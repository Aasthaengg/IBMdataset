def f(n):
    k = 0
    while n*2**k<K:
        k += 1
    return k
N,K = map(int,input().split())
if K<=N:
    P = (N-K+1)/N
    for i in range(1,K):
        P += 2**(-f(i))/N
else:
    P = 0
    for i in range(1,N+1):
        P += 2**(-f(i))/N
print(P)