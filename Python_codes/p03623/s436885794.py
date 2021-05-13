X, A, B = map(int, input().split())
D = {abs(X-A):"A", abs(X-B):"B"}

print(D[min(abs(X-A), abs(B-X))])