import sys
import bisect
sys.setrecursionlimit(10**7)

n,m=map(int,input().split())
a=list(map(int,input().split()))

a.sort()

def hantei(t):
    global n,m,a
    ret = 0
    for sa in a:
        ret += n - bisect.bisect_left(a,t-sa)
    if ret<=m:return True
    else:return False

def nibun(l,r):
    if r == l:
        return l
    f = (l+r)//2
    if hantei(f):
        return nibun(l,f)
    else:
        return nibun(f+1,r)


p=nibun(0,3*(10**5))

a.reverse()
na=[]
sna = 0
for sa in a:
    sna += sa
    na.append(sna)
na.reverse()
na.append(0)
a.reverse()

res = 0
f=0
for sa in a:
    q = bisect.bisect_left(a,p-sa)
    f += n-q
    res += na[q]+sa*(n-q)
res += (p-1)*(m-f)

print(res)