X = list(map(int, input().split()))
X.sort()
K = int(input())

print(X[0] + X[1] + (X[2] * (2 ** K)))