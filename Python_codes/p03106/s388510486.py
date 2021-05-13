import math
A,B,M = map(int,input().split())
C = math.gcd(A,B)
ls = []
for i in range(1,101):
    if C % i == 0:
        ls.append(i)
ls.sort()
print(ls[-M])