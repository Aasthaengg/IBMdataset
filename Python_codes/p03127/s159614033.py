import math
N=int(input())
A=list(map(int,input().split()))

def agcd(l):
    a=math.gcd(l[0],l[1])
    for i in range(2,len(l)):
        a=math.gcd(a,l[i])
    return a

print(agcd(A))