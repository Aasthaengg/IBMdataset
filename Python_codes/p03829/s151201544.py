N, A, B = map(int, input().split())
X = list(map(int, input().split()))

c = 0 
for i in range(len(X) - 1):
    tmp = X[i+1] - X[i]
    c += min(A*tmp, B)

print(c)
