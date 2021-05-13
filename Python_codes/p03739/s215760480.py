import sys
from collections import Counter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
a=lmp()
s=0
ans1=0
ans2=0
for i in range(n):
    if i%2==0:
        s+=a[i]
        if s>=0:
            ans1+=s-(-1)
            s=-1
    else:
        s+=a[i]
        if s<=0:
            ans1+=1-s
            s=1

s=0
for i in range(n):
    if i%2==1:
        s+=a[i]
        if s>=0:
            ans2+=s-(-1)
            s=-1
    else:
        s+=a[i]
        if s<=0:
            ans2+=1-s
            s=1
print(min(ans1,ans2))