import sys
import math
def input():
    return sys.stdin.readline()[:-1]

n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]

def check(m):
    tmp=0
    for i in range(n):
        if (h[i]-b*m)/(a-b)>0:
            tmp+=math.ceil((h[i]-b*m)/(a-b))
    if tmp<=m:
        return True
    else:
        return False

low=0
high=max(h)
while high-low>1:
    mid=(low+high)//2
    if check(mid):
        high=mid
    else:
        low=mid
    # print(low)
    # print(high)
print(high)