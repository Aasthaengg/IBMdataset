import sys
input = sys.stdin.readline

n,m=map(int,input().split())
L=list(map(int,input().split()))

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

def count2(x):
    c=0
    while x%2==0:
        x//=2
        c+=1
    return c

c2=count2(L[0])
LCM = 1

for i in L:
    if count2(i)!=c2:
        print(0)
        sys.exit()
    LCM = lcm(i//2,LCM)
    if LCM>m:
        print(0)
        sys.exit()
print(max(0,(m-LCM)//(2*LCM)+1))


