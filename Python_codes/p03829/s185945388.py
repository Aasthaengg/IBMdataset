N, A, B = map(int, input().split())
X = [int(x) for x in input().split()]
ans = 0
for x,y in zip(X[:N-1],X[1:]):
    if (y-x) * A < B:
        ans += (y-x) * A
    else:
        ans += B
print(ans) 