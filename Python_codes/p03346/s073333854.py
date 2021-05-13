N = int(input())
A = [0 for _ in range(N+1)]
for _ in range(N):
    a = int(input())
    if A[a-1]==0:
        A[a] = 1
    else:
        A[a] = A[a-1]+1
n = max(A)
print(N-n)