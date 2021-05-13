N, A, B = map(int, input().split())
X = tuple(map(lambda x: int(x) * A, input().split()))
print(sum(min(X[i] - X[i - 1], B) for i in range(1, N)))
