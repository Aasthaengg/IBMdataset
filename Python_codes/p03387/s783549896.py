X = list(map(lambda x: int(x), input().split(" ")))
X.sort()

print(X[2] - X[1] + int((X[1] - X[0]) / 2) + 2 * ((X[1] - X[0]) % 2))