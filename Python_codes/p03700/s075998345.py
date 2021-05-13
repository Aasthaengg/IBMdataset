import sys
import math
def input():
    return sys.stdin.readline()[:-1]

n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]

low,high=0,10**9+1
while high-low>1:
    mid=(high+low)//2
    cnt=0
    for i in range(n):
        tmp=h[i]-mid*b
        if tmp>0:
            cnt+=math.ceil(tmp/(a-b))
    if cnt<=mid:
        high=mid
    else:
        low=mid
    # print(high,low)
print(high)