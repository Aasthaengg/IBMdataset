ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys
n,m = ma()
ckp = []
st = []

for i in range(n):
    st.append(lma())
for i in range(m):
    ckp.append(lma())
for a,b in st:
    tmp=10**15
    ans=0
    for i  in range(m):
        c,d=ckp[i]
        if tmp>abs(a-c)+abs(b-d):
            tmp=abs(a-c)+abs(b-d)
            ans=i+1
    print(ans)
