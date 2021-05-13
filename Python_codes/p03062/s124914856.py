
N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    if A[i] < 0:
        A[i] *= -1
        A[i+1] *= -1

    #print(A)

if A[N-1] >= 0:
    print(sum(A))
    exit()

A = A[::-1]
A[0] *= -1
idx = A.index(min(A))
#print(idx)
A[0] *= -1

for i in range(0, idx):
    if A[i] < 0:
        A[i] *= -1
        A[i+1] *= -1

    #print(A)
    
print(sum(A))