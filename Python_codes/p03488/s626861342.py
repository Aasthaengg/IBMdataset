s=input()
X,Y=map(int,input().split())
from collections import defaultdict
def solve(da,dp,G):
    for i in range(len(da)):
        tmp=set()
        for j in dp:
            tmp.add(j-da[i])
            tmp.add(j+da[i])
        dp=tmp
    if G in dp:
        return True
    else:
        return False
    """amax=0
    for i in a:
        amax+=abs(i)
    if amax==0:
        if G==0:
            return True
        else:
            return False
    if a[0]==G:
        return True
    dp=[[0]*2*amax for _ in range(3)]
    dp[0][a[0]]=1
    for i in range(1,len(a)):
        p=a[i]
        for j in range(-amax,amax):
            dp[i%3][j-p]+=dp[(i-1)%3][j]
            dp[i%3][j+p]+=dp[(i-1)%3][j]
            #print(dp)
        if dp[i%3][G]>=1:
            return True
    return False"""
    """#print(a)
    dp=set()
    dp.add(a[0])
    dp2=set()
    for i in range(1,len(a)):
        for j in dp:
            dp2.add(j-a[i])
            dp2.add(j+a[i])
        dp=copy.deepcopy(dp2)
    #print(dp)
    if G in dp:
        return True
    return False"""

d=[len(x) for x in s.split("T")]

dx=d[2::2]
dy=d[1::2]

if solve(dx,{d[0]},X) and solve(dy,{0},Y):
    print("Yes")
else:
    print("No")
