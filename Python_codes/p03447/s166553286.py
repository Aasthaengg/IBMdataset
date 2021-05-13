X, A, B = [int(input()) for _ in range(3)]
X -= A
print(X - B * (X // B))