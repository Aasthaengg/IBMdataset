N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = []
total = sum(A)

for i in range(len(B)):
    if A[i] >= B[i]:
        t = A[i] - B[i]
        A[i] = t
    else:
        t = B[i] - A[i]
        A[i] = 0
        
        if A[i+1] >= t:
            A[i+1] = A[i+1] - t
        else:
            A[i+1] = 0
print(total - sum(A))