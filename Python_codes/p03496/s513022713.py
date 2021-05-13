N = int(input())
A = list(map(int, input().split()))
if abs(max(A)) >= abs(min(A)):
    max_idx = A.index(max(A))
    print(2 * N - 1)
    for i in range(N):
        print(max_idx + 1, i + 1)
    for i in range(N - 1):
        print(i + 1, i + 2)
else:
    min_idx = A.index(min(A))
    print(2 * N - 1)
    for i in range(N):
        print(min_idx + 1, i + 1)
    for i in range(N, 1, -1):
        print(i, i - 1)
