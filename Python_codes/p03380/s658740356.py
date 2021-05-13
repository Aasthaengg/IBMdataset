N = int(input())
A = list(map(int,input().split()))

A = sorted(A)
B = A[::]
n = A[-1]
temp = n // 2
min_ = 10 ** 9 + 7
for i in range(N - 1):
    A[i] -= temp
    A[i] = abs(A[i])
min_ = min(A)
for i in range(N - 1):
    if A[i] == min_:
        ans = B[i]
print(n, ans)