a, b, m = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
X = []
Y = []
C = []
for i in range(m):
    x, y, c = [int(j) for j in input().split()]
    X.append(x)
    Y.append(y)
    C.append(c)
# print(X, Y, C)

pricelist = [min(A) + min(B)]
for i in range(m):
    pricelist.append(A[X[i]-1] + B[Y[i]-1] - C[i])
print(min(pricelist))
