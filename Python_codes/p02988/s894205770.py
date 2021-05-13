import math
def ip():return int(input())
def inp():return map(int,input().split())
def linp():return list(map(int,input().split()))

n=ip()
p=linp()
ans=0
for i in range(1,n-1):
    l=[p[i-1],p[i],p[i+1]]
    if p[i]>min(l) and p[i]<max(l):ans+=1
print(ans)

