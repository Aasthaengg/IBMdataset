def gcd(A, B)->int:
  A = A % B
  if A == 0:
    return B
  else:
    return gcd(B, A)
    

A, B = list(map(int, input().split()))
N = (A*B)/gcd(A, B)
 
print(int(N))