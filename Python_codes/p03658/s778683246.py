N, K = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
X=X[::-1]
print(sum(X[:K]))
