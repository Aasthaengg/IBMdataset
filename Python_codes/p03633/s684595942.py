import math
def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)
def lcm(x,y):
    return x*y//gcd(x,y)
N = int(input())
if N == 1:
    print(int(input()))
else:
    ans = int(input())
    for i in range(N-1):
        J = int(input())
        ans = lcm(ans,J)
    print(ans)