from math import gcd
A, B, C, D = map(int, input().split())
E = C*D//gcd(C, D)

c1 = (B//C)-((A+C-1)//C)+1
c2 = (B//D)-((A+D-1)//D)+1
c3 = (B//E)-((A+E-1)//E)+1
ans = B-A+1-c1-c2+c3

print(ans)
