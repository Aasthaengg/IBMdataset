import math
def LCM(X,Y):
    return (X*Y)//math.gcd(X,Y)
  
N = int(input())
A = [int(input()) for T in range(0,N)]
TLCM = 1
for T in range(0,N):
    TLCM = LCM(TLCM,A[T])
print(TLCM)