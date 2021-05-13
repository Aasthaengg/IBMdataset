import math
def ip():return int(input())
def inp():return map(int,input().split())
def inpstr():return map(str,input().split())
def linp():return list(map(int,input().split()))
def linpstr():return list(map(str,input().split()))

n=ip()
v=linp()
c=linp()
ans=0
for i in range(n):
    if v[i]>c[i]:ans+=v[i]-c[i]
print(ans)