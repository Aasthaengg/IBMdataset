W, a, b = map(int, input().split())
A = [a, a + W]
B = [b, b + W]
if A[1] < B[0]:
    print(B[0] - A[1])
elif B[1] < A[0]:
    print(A[0] - B[1])
else:
    print(0)