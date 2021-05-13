N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

m = 0
for i in range(N):
    if A[i] >= B[i]:
        m += B[i]
    else:
        m += A[i]
        if A[i+1] >= (B[i]-A[i]):
            m += (B[i]-A[i])
            A[i+1] -= (B[i]-A[i])
        else:
            m += A[i+1]
            A[i+1] = 0
        
print(m)