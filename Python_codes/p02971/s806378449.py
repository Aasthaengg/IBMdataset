N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A,reverse=True)
b0 = B[0]
b1 = B[1]
for i in range(N):
    a = A[i]
    if a!=b0:
        print(b0)
    else:
        print(b1)