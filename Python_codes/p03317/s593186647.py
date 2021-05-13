import math

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
# print(N, K, A)

answer = math.ceil((N - 1)/ (K - 1))

print(answer)
