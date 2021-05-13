N = int(input())
A = [0] + list(map(int, input().split()))
x = [0] + [0]*N

# x[i+1] = 2*A[i] - x[i]
S = sum(A)
x[1] = S - 2 * (sum([A[i] for i in range(2, N, 2)]))
for i in range(2, N+1):
    x[i] = 2*A[i-1] - x[i-1]

print(*x[1:])
