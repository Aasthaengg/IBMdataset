N = int(input())
B = list(map(int, input().split()))

A=[10**6]*N

for i in range(N-1):
    if A[i] >= B[i]:
        A[i] = B[i]
    if A[i+1] >= B[i]:
        A[i+1] = B[i]

print(sum(A))