X = list(map(lambda x: int(x), input().split(" ")))
K = int(input())

X.sort()

print(X[0] + X[1] + X[2] * (2 ** K))