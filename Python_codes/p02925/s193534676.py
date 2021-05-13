from subprocess import*
call(('pypy3','-c',"""
import sys
from collections import*
from itertools import*
input=sys.stdin.readline
n=int(input())
d=defaultdict(count().__next__)
es=[]
for i in range(1,n+1):
    *a,=map(int,input().split())
    for j,k in zip(a,a[1:]):
        x,y=i,j
        if y<x:x,y=y,x
        v,w=i,k
        if w<v:v,w=w,v
        es+=(d[x*n+y],d[v*n+w]),
s=len(d)
outs=[[]for _ in range(s)]
ins=[0]*s
f=set(range(s))
for i,j in es:
    outs[i]+=j,
    f-={j}
    ins[j]+=1
q=deque(f)
l=0
data=[0]*s
m=0
while q:
    i=q.popleft()
    l+=1
    t=data[i]+1
    if t>m:m=t
    for j in outs[i]:
        if ins[j]>1:ins[j]-=1
        else:q+=j,
        if t>data[j]:data[j]=t
print(-(l<s)or m)
"""))