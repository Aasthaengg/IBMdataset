A = list(map(int, input().split()))
A = sorted(A, reverse=True)
if A[0] == A[1] + A[2]:
    print("Yes")
else:
    print("No")