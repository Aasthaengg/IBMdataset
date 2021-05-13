N = int(input())
A = list(map(int, input().split()))

S = sum(A)

suma = 0
for i in range(1,N,2):
    suma += A[i]

X1 = S - 2 * suma
ans = [X1]

prev = X1
for i in range(0, N-1):
    nx = 2 * A[i] - prev
    ans.append(nx)
    prev = nx

print(*ans)