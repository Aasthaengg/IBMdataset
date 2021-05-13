N = int(input())
Ap = [int(x) for x in input().split()]
A = sorted([Ap[i]  -i-1 for i in range(N)])

if N % 2 != 0:
    b = A[(N+1)//2 - 1]
    print( sum( [abs(x-b) for x in A] ) )
else:
    mf,mb = A[N//2-1], A[N//2]
    if mb - mf >= 2:    b = mb -1
    else:  b = mb
    print( sum( [abs(x-b) for x in A] ) )
