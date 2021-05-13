
N = int(input())
A = list(map(int, input().split()))
A = [0] + A

x = [0] * (N+1)
#print(A[1:N+1:2])
#print(A[2:N:2])
x[1] = sum(A[1:N+1:2]) - sum(A[2:N:2])
for i in range(1, N):
    x[i+1] = 2 * A[i] - x[i]

print(" ".join(map(str, x[1:])))