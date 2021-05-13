import math
n=int(input())
t=[int(input()) for _ in range(n)]
#print(t)
if n==1:
    print(t[0])
    exit()

for i in range(n-1):
    if i==0:
        lcm=(t[i]*t[i+1])//math.gcd(t[i],t[i+1])
    else:
        lcm=(lcm*t[i+1])//math.gcd(lcm,t[i+1])
print(lcm)