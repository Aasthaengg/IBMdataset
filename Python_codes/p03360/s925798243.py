X = list(map(int, input().split()))
K = int(input())


X.sort(reverse=True)
for i in range(K):
    X[0] = X[0]*2

print(sum(X))
