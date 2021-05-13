X = list(map(int,input().split()))

X = sorted(X, reverse=True)
print(X[0]*10 + X[1] + X[2])