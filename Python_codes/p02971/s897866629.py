N = int(input())
A = [int(input()) for i in range(N)]
A_ = sorted(A)
max1 = A_[-1]
max2 = A_[-2]

for i in range(N):
    if A[i] == max1:
        print(max2)
    else:
        print(max1)