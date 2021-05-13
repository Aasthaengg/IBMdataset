def factmod(n):
    tmp = 1
    for i in range(1,n+1):
        tmp *= i
        tmp %= (10**9+7)
    return tmp   
N,M = list(map(int,input().split()))
if abs(N-M) > 1:
    print(0)
    exit()
if N == M:
    print((2*(factmod(N)*factmod(M))%(10**9+7)))
else:
    print(factmod(N)*factmod(M)%(10**9+7))