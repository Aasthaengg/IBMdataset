A = list(map(int, input().split()))
a = A[1]//A[0]
if a <= A[2]:
    print(a)
else:
    print(A[2])