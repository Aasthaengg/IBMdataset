n = int(input())
A = list(map(int, input().split()))
tot = sum([abs(A[i] - A[i - 1]) if i != 0 else abs(A[0]) for i in range(n)]) + abs(A[-1])
A = [0, ] + A + [0, ]
for i in range(1, n + 1):
    if min(A[i - 1], A[i + 1]) <= A[i] <= max(A[i - 1], A[i + 1]):
        print(tot)
    else:
        print(tot - (abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i]) - abs(A[i + 1] - A[i - 1])))
