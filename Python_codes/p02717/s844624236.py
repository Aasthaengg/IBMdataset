ri = lambda S: [int(v) for v in S.split()]
X, Y, Z = ri(input())

X, Y = Y, X
X, Z = Z, X

print(X, Y, Z, sep=" ")