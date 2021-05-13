N = int(input())

a = list(str(N))
a = [int(s) for s in a]


Z = 10 ** (len(a) - 1)

Y = N - Z

X = list(str(Y))
X = [int(s) for s in X]
SUM = 0
for i in range(len(X)):
    SUM = SUM + X[i]

if Y != 0:
    print(SUM + 1)
else:
    print(10)