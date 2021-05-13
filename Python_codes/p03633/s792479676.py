import math
def lcm(l: list):
    n=len(l)
    lcm=(l[0]*l[1])//math.gcd(l[0],l[1])
    for i in range(2,n):
        lcm=(l[i]*lcm)//math.gcd(l[i],lcm)

    return lcm

n=int(input())
t=[]
for i in range(n):
    t.append(int(input()))

if n==1:
    print(t[0])
else:
    print(lcm(t))