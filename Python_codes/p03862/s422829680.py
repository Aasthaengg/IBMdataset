N, X = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

cost = max(0, A[0] + A[1] - X)
A[1] = max(0, A[1] - cost)

for i in range(2, N):
    cost += max(0, A[i - 1] + A[i] - X)
    A[i] = max(0, A[i] - max(0, A[i - 1] + A[i] - X))

print(cost)
