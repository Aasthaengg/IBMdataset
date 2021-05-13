import math
def LCM(A):
    X = A[0]
    for I in range(1,len(A)):
        X = (X*A[I])//math.gcd(X,A[I])
    return X
  
N = int(input())
A = [int(I) for I in input().split()]
MAX = LCM(A)-1
FA  = [MAX%I for I in A]
print(sum(FA))