X = list(map(int, input().split()))

f = max(X)
g = min(X)

if X.count(f) < X.count(g):
    print(f)
else:
    print(g)
