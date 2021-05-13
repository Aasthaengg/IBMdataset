N = int(input())
A = input().split()
L = A[1::2]
R = A[0::2]
if N%2==0:
    print(' '.join(L[::-1]+R))
else:
    print(' '.join(R[::-1]+L))