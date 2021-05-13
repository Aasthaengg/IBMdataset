A = list(map(int, input().split()))
A = sorted(A)
if any([a % 2 == 0 for a in A]):
    print(0)
else:
    print(A[0] * A[1])