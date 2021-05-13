S = int(input())
A = [0] * (2001)
A[3] = 1
mod = 10**9+7
for i in range(4, S+1):
    A[i] = A[i-1] + A[i-3]
    A[i] %= mod
print(A[S])
