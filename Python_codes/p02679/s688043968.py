import sys
import collections
import fractions
import math
def input():
    return sys.stdin.readline()[:-1]
n=int(input())
zero = 0
dic = {}
mod = 10**9+7
for i in range(n):
    a,b = map(int,input().split())
    rt =0
    if a==0 and b==0:
        zero+=1
        continue
    g = math.gcd(a,b)
    a = a//g
    b = b//g
    if b<0:
        a=-a
        b=-b
    if a<0 and b==0:
        a=-a
        b=-b
    if a<=0:
        rt=1
        a,b = b,-a

    if (a,b) not in dic:
        if rt==0:
            dic[(a,b)] = [1,0]
        else:
            dic[(a,b)] = [0,1]
    else:
        if rt==0:
            dic[(a,b)][0] += 1
        else:
            dic[(a,b)][1] += 1

ans = 1
for i,j in dic.values():
    tmp = pow(2,i,mod) - 1
    tmp2 = pow(2,j,mod) - 1
    su = (tmp+tmp2+1)%mod
    ans = (ans*su)%mod

ans = (ans-1+zero)%mod

print(ans)
