import math
def ip():return int(input())
def inp():return map(int,input().split())
def inpstr():return map(str,input().split())
def linp():return list(map(int,input().split()))
def linpstr():return list(map(str,input().split()))

a,b=inp()
ans=0
if a<b:a,b=b,a
ans+=a
a=a-1
if a<b:a,b=b,a
ans+=a
print(ans)
