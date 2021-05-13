import math
def lcm(x,y):
    return x*y//math.gcd(x,y)
    

N = int(input())
T = int(input())
for i in range(1,N):
    S = int(input())
    T = lcm(S,T)
print(T)