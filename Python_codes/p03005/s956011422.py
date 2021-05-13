(N, K) = list(map(int, input().split()))
max_distribution = N - K
if K == 1:
    max_distribution = 0
print(max_distribution)
