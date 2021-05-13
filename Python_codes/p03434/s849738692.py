N = int(input())
A = [int(i) for i in input().split()]

A.sort(reverse=True)

print( sum(A[::2]) - sum(A[1::2]) )

