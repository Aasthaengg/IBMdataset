X = list(map(int, input().split()))

n=10
for i in range(len(X)):
    if X[i] == 0:
        n = i

print(n+1)