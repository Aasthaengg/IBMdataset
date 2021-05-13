import math
A,B = input().split()
A = int(A)
B = int(B)
x = int(math.gcd(A,B))
print((A*B)//x)
