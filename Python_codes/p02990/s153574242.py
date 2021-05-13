N, K = map(int, input().split())
def comb(n, r, p):
    X, Y = 1, 1
    for i in range(r):
        X *= n-i
        Y *= i+1
        X %= p
        Y %= p
    return int(X * pow(Y, p-2, p))
def func(i):
    if N - K + 1 < i:
        return 0
    p = 10**9 + 7
    ans = comb(n=K-1, r=i-1, p=p) * comb(n=N-K+1, r=i, p=p) % p
    return ans

for i in range(1, K+1):
    if i==1:
        # from math import factorial
        print(N-K+1)
    else:
        print(func(i))