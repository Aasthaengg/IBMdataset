N = int(input())
A = [int(input()) for i in range(N)]

maximum = max(A)
count_max = A.count(maximum)
if count_max > 1:
    for i in range(N):
        print(maximum)
else:
    for i in range(N):
        if A[i] != maximum:
            print(maximum)
        else:
            num = A[i]
            A[i] = 0
            print(max(A))
            A[i] = num
