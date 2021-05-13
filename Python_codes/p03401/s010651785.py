N = int(input())
A = list(map(int,input().split()))
A = [0] + A + [0]
SUM = 0
for i in range(N+1):
    SUM += abs(A[i+1] - A[i])
for i in range(1,N+1):
    if (A[i] - A[i-1]) * (A[i+1] - A[i]) >= 0:
        ans = SUM
    else:
        ans = SUM - 2 * min(abs(A[i] - A[i-1]), abs(A[i+1] - A[i]))
    print(ans)