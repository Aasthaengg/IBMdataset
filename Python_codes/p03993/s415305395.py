N = int(input())
A = list(map(int, input().split()))

print([A[i] - 1 > i and A[A[i] - 1] - 1 == i for i in range(N)].count(1))