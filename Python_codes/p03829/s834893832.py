N, A, B = map(int, input().split())
X = list(map(int, input().split()))
sum = 0
for x in range(len(X) -1):
    ds = X[x+1] - X[x]
    sum += min(ds * A, B)

print(sum)