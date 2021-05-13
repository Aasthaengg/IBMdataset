N = int(input())
B = list(map(int, input().split()))

A = [10**5]*N

for i in range(N-1):
    A[i] = min(A[i], B[i])
    A[i+1] = min(A[i+1], B[i])

print(sum(A))
