N = int(input())
A = tuple(map(int, input().split()))

M, m = max(A), min(A)

print(2 * N - 2)
if abs(M) >= abs(m):
    ind = A.index(M)
    for x in set(range(N)) - {ind}:
        print(ind + 1, x + 1)
    for x in range(1, N):
        print(x, x + 1)
else:
    ind = A.index(m)
    for x in set(range(N)) - {ind}:
        print(ind + 1, x + 1)
    for x in range(N - 1, 0, -1):
        print(x + 1, x)
