import math
def lcm(l):
    r=l.pop(0)
    for i in l:
        r=r*i//math.gcd(r,i)
    return r

N=int(input())
T=[]
for i in range(N):
    T.append(int(input()))
print(lcm(T))