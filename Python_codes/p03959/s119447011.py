import bisect
import sys
import math
import itertools
sys.setrecursionlimit(10000)

INF = float('inf')

# input macro
def i():
    return int(raw_input())
def ii():
    return map(int,raw_input().split(" "))
def s():
    return raw_input()
def ss():
    return raw_input().split(" ")
def slist():
    return list(raw_input())
def join(s):
    return ''.join(s)

#memoize macro
def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[(args)] = f(*args)
        return cache[args]
    return helper

nh=zip([1,0,-1,0],[0,1,0,-1])
mod=1000000007

###########
n=i()
t=ii()
a=ii()
just=[0]*n
ub=[INF]*n
lb=[0]*n

def justa(x,y):
    if just[x] in [0,y]:
        just[x]=y
    else:
        print '0'
        sys.exit()

justa(0,t[0])
justa(n-1,a[n-1])

for j in range(1,n):
    if t[j]!=t[j-1]:
        justa(j,t[j])
    else:
        ub[j]=t[j]
for j in reversed(range(0,n-1)):
    if a[j]!=a[j+1]:
        justa(j,a[j])
    else:
        ub[j]=min(ub[j],a[j])

ans=1
for j in range(1,n):
    if just[j]==0:
        ans=ans*ub[j]%mod
    elif just[j]<=ub[j]:
        ans=ans
    else:
        print '0'
        sys.exit()

print ans
    
