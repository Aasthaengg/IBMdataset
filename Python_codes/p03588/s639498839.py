N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
X = max(A)[:]
print(X[0] + X[1])