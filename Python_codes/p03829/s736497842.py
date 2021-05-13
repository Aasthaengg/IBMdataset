N, A, B = list(map(int, input().split()))
X = list(map(int, input().split()))
Sum = 0
for i in range(1, N):
    Sum += min((X[i] - X[i - 1]) * A, B)

print(Sum)
