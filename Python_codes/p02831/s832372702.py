import math
A,B = (int(x) for x in input().split())
print(A*B//math.gcd(A,B))