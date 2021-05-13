N = int(input())
A = list(map(int,input().split()))
A_copy = A.copy()
n = N//2
A.sort()
avg = (A[n]+A[n-1])/2
for i in A_copy:
    if i < avg:
        print(A[n])
    else:
        print(A[n-1])