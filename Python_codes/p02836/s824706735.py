import math
from collections import defaultdict
ml=lambda:map(float,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())

"""========main code==============="""

s=ip()
ans=0
for i in range(len(s)//2):
    if(s[i]!=s[len(s)-1-i]):
        ans+=1
print(ans)        