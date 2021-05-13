n = int(input())
A = [list(map(int, list('{:020b}'.format(a))))
     for a in map(int, input().split())]

ans = 0
R = 0
X = [0]*20
for L in range(n):
    while R < n and all(x+y != 2 for x, y in zip(X, A[R])):
        for i in range(20):
            X[i] += A[R][i]
        R += 1
    ans += R-L
    for i in range(20):
        X[i] -= A[L][i]
print(ans)