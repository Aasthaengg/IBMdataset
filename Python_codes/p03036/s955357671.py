r, D, x2k = [int(n) for n in input().split()]
X = [x2k]
for i in range(10):
    X.append(r*X[i]-D)
    print(X[i+1])
