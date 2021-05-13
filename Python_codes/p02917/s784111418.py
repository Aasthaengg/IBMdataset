N = int(input())
B = [int(i) for i in input().split(' ')]
A = [0]*(N)
for i,a in enumerate(B):
    if i == 0: #index最初
        A[i] = a
        A[i+1] = a
    else:#二番目以降
        if B[i-1] < B[i]:
            A[i+1] = a
        else:
            A[i] = a
            A[i+1] = a

print(sum(A))