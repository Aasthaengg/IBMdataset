N, A, B = map(int, input().split())
X = list(map(int, input().split()))

S = 0
for i in range(1, N):
    if A * (X[i] - X[i - 1]) <= B:
        S += A * (X[i] - X[i - 1])
    else:
        S += B
print(S)