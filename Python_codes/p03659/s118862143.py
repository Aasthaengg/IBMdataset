from itertools import accumulate


N = int(input())
A = list(accumulate(map(int, input().split())))
print(min(abs(A[N - 1] - 2 * A[i]) for i in range(N - 1)))
