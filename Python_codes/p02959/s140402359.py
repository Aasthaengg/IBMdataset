N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0
temp = 0
for i in range(N):
    if B[i] <= A[i]:
        res += B[i]
    else:
        res += A[i]
        res += B[i]-A[i] if A[i+1] - (B[i]-A[i]) >= 0 else A[i+1]
        A[i+1] = max(A[i+1] - (B[i]-A[i]), 0)
print(res)