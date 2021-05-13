import math
A, B, C = list(map(lambda n: int(n), input().split(" ")))
 
print("YES") if C % math.gcd(A,B) == 0 else print("NO")