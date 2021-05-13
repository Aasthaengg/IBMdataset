k=int(input())
import math
def ggcd(a,b,c):
    return math.gcd(math.gcd(a,b),math.gcd(a,c))
a=0
for i in range(1,1+k):
    for j in range(1,1+k):
        for l in range(1,1+k):
            a+=ggcd(i,j,l)
print(a)