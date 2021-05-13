N = int(input())
A = list(map(int, input().split()))

A_even = A[0:N:2]
A_odd = A[1:N:2]

X = []
if N % 2 == 1:
    X.append(sum(A_even) - sum(A_odd))
else:
    X.append(sum(A_even) - sum(A_odd))
for i in range(1, N):
    X.append(2*A[i-1] - X[i-1])
    
print(*X)