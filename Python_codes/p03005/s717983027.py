N, K = list(map(int, input().split()))
answer = 0 if K == 1 else N - (K - 1) - 1
print(answer)
