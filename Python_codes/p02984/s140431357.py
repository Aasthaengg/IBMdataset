N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
X = []
X.append(sum_A - 2*(sum(A[1:N-1:2])))
for i in range(1, N):
    X.append(2*A[i-1] - X[i-1])

print(*X)