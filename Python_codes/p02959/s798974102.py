N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

allenemy = sum(A)
for i in range(N):
    A[i] -= B[i]
    if A[i] < 0:
        A[i+1] += A[i]
        A[i] = 0
        if A[i+1] < 0:
            A[i+1] = 0
print(allenemy - sum(A))