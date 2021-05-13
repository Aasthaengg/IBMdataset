N = int(input())
A = [int(input()) for _ in range(N)]
sorted_A = sorted(A)
[print(sorted_A[-2] if sorted_A[-1] == A[i] else sorted_A[-1]) for i in range(N)]
