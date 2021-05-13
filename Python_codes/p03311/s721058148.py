N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= i + 1
A.sort()
if N % 2:
    median = A[N // 2]
    print(sum(abs(a - median) for a in A))
else:
    median1 = A[N // 2 - 1]
    median2 = A[N // 2]
    print(min(sum(abs(a - median1) for a in A), sum(abs(a - median2) for a in A)))
