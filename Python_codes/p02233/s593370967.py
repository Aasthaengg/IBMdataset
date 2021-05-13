n = int(input())

A = []
A.append(1)
A.append(1)

if n>1:
    for i in range(n-1):
        A.append(A[i]+A[i+1])

print(A[n])
