ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

def modinv(a,p):
    b,u,v = p,1,0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -=t*v
        u,v = v,u
    u %=p
    return u
n,p = ma()
s = input();s=s[::-1]

if p==2:
    ans=0
    for i in range(n):
        if int(s[i])%2==0:
            ans+=n-i
    print(ans)
    exit()
if p==5:
    ans=0
    for i in range(n):
        if int(s[i])%5==0:
            ans+=n-i
    print(ans)
    exit()

iv10 = modinv(10,p)
ls = [0]*n
for i in range(n):
    a = int(s[i])
    ls[i]=(ls[i-1]+a*pow(10,i,p))%p
co = collections.Counter(ls)
ans=co[0]
tmp=0
for i in range(0,n-1):
    a = int(s[i])
    co[ls[i]%p]-=1
    tmp = (tmp +a)*iv10%p
    r = tmp*pow(10,i+1,p)%p
    ans +=co[r]
print(ans)
