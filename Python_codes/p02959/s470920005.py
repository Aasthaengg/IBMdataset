N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

monster = sum(A)
for i in range(N):
    t = A[i] - B[i]
    if t < 0:
        A[i] = 0
        if A[i+1] + t < 0:
            A[i+1] = 0
        else:
            A[i+1] += t
    else:
        A[i] = A[i] - B[i]

print(monster - sum(A))