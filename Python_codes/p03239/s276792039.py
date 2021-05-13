import math
def ip():return int(input())
def imp():return map(int,input().split())

n,t=imp()
ans=10**18
for _ in range(n):
    c,d=imp()
    if d<=t:
        ans=min(ans,c)
if ans==10**18:print("TLE")
else:print(ans)