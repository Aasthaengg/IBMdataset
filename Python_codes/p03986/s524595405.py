import sys
from collections import Counter
from collections import deque
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

x=list(input())
n=len(x)
l=[]
for i in range(n):
    if x[i]=="S":
        l.append("S")
    else:
        if len(l)==0:
            l.append("T")
        elif l[-1]=="S":
            l.pop()
        else:
            l.append("T")
print(len(l))