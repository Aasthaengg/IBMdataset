import math
def ip():return int(input())
def inp():return map(int,input().split())
def inpstr():return map(str,input().split())
def linp():return list(map(int,input().split()))
def linpstr():return list(map(str,input().split()))

n,m=inp()
l=[0]*m
for _ in range(n):
    a=linp()
    for i in range(1,a[0]+1):
        l[a[i]-1]+=1

ans=0
for x in l:
    if x==n:ans+=1
print(ans)