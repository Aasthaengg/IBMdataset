K,T = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
if T == 1:
    print(A[0] - 1)
else:
    print(max(0, A[-1] - (K - A[-1] + 1)))