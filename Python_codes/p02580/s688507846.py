import sys
import  math
import fractions
from collections import defaultdict
import heapq
from bisect import bisect_left,bisect

stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

H,W,M=nm()
r=[0]*(10**6)
c=[0]*(10**6)
mass=set()
for i in range(M):
    h,w=nm()
    mass.add(H*h+w)
    r[h]+=1
    c[w]+=1

rl=[]
cl=[]

r_max=0
for i in range(1,H+1):
    r_max=max(r[i],r_max)
    
c_max=0
for i in range(1,W+1):
    c_max=max(c[i],c_max)

for i in range(1,H+1):
    if(r[i]==r_max):
        rl.append(i)

for i in range(1,W+1):
    if(c[i]==c_max):
        cl.append(i)



for i in rl:
    for j in cl:
        if(i*H+j not in mass):
            print(r_max+c_max)
            sys.exit(0)


print(r_max+c_max-1)
