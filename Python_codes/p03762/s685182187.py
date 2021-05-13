def d_igeta(N, M, X, Y):
    tmp1 = 0
    tmp2 = 0
    for k, x in enumerate(X):
        k += 1
        tmp1 += (k - 1) * x - (N - k) * x
    for k, y in enumerate(Y):
        k += 1
        tmp2 += (k - 1) * y - (M - k) * y
    return (tmp1 * tmp2) % (10**9 + 7)

N,M = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
Y = [int(i) for i in input().split()]
print(d_igeta(N, M, X, Y))