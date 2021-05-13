N, A, B = map(int, input().split())
X = list(map(int, input().split()))
dist = [x2 - x1 for x1, x2 in zip(X, X[1:])]
print(sum(min(B, A*d) for d in dist))