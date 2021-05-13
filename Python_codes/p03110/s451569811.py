import math
def ip():return int(input())
def inp():return map(int,input().split())
def inpstr():return map(str,input().split())
def linp():return list(map(int,input().split()))
def linpstr():return list(map(str,input().split()))

yen=0
coin=0
ans=0
for _ in range(ip()):
    x,u=inpstr()
    x=float(x)
    if u=="BTC":x=x*380000.0
    ans+=x
print(ans)