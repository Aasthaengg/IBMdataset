#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,cos,radians,sqrt
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n=I()
bekit=[0 for i in range(n+1)]
bekit[0]=1
for i in range(n):
    bekit[i+1]=(bekit[i]*2)%mod
#print(bekit)
countz=0
countx=0
county=0
nump=[]
numm=[]
for i in range(n):
    a,b=MI()
    if a==0 and b==0:
        countz+=1
    elif a==0:
        if b<0:
            b*=(-1)
        countx+=1
    elif b==0:
        if a<0:
            a*=(-1)
        county+=1
    elif a*b<0:
        #print(a,b)
        if b<0:
            a*=(-1)
            b*=(-1)
        g=gcd(abs(a),b)
        a=a//g
        b=b//g
        #print(a,b)
        numm.append([a,b])
    else:
        g=gcd(abs(a),abs(b))
        a//=g
        b//=g
        nump.append([abs(a),abs(b)])
#print(nump)
#print(numm)
nump=list(map(tuple,nump))
numm=list(map(tuple,numm))
u=Counter(nump)
v=Counter(numm)
#print(u)
#print(v)
nums=[]
pairs=[]
for k in u.keys():
    vz=((-1)*k[1],k[0])
    s=u[k]
    t=v[vz]
    #print(vz)
    #print(s)
    #print(t)
    if t>0:
        nums.append([s,t])
        pairs.append(s+t)
#print(nums)
#print(nums)
#print(n-sum(pairs)-countx-county-countz)
#print(pairs)
#print(n-sum(pairs)-countx-county-countz)
if countx>0 and county>0:
    cou=countx+county
else:
    cou=0
ans=bekit[n-sum(pairs)-cou-countz]
#print(ans)
for j in range(len(nums)):
    q=bekit[nums[j][0]]
    p=bekit[nums[j][1]]
    #print(q)
    #print(p)
    ans=(ans*(q+p-1))%mod
if countx>0 and county>0:
    ans=(ans*(bekit[countx]+bekit[county]-1))%mod
ans-=1
if countz>0:
    ans+=countz%mod
print(ans%mod)
