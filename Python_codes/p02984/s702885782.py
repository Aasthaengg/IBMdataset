n = int(input())
A = list(map(int,input().split()))
x = [0]*n
S = sum(A)
A2 = A[1::2]
x[0] = S - 2*sum(A2)
for i in range(n-1):
    x[i+1] = 2*A[i]-x[i]
print(*x)