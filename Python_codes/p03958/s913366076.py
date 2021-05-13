K, T = map(int, input().split())
A = [int(i) for i in input().split()]

A = sorted(A, reverse=True)
while len(A) > 1:
    A[0] -= 1
    A[-1] -=1
    if A[0] == 0:
        del A[0]
    if A[-1] == 0:
        del A[-1]

if A:
    print(A[0]-1)
else:
    print(0)
