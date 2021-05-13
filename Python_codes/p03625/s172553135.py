import sys
from collections import Counter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
a=sorted(lmp(),reverse=True)
i=0
l=[]
while i<n-1:
    if a[i]==a[i+1]:
        l.append(a[i])
        i+=1
    i+=1
if len(l)>=2:
    print(l[0]*l[1])
else:
    print(0)