N = int(input())
K = int(input())
X = int(input())
Y = int(input())


if N < K:
    sum_a = X * N
    sum_b = 0
else:
    sum_a = X * K
    sum_b = Y * (N-K)

print(sum_a + sum_b)
