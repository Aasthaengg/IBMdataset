N = int(input())
A = list(map(int, input().split()))
X = [sum(A) - 2 * sum(A[i] for i in range(1, N, 2))]
for i in range(N - 1):
    X.append(2 * A[i] - X[-1])
print(*X)
