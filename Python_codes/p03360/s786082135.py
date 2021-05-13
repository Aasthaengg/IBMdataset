A=input().split()
A = [int(s) for s in A]
K=int(input())
A.sort()
print(A[2]*2**K+A[0]+A[1])