import math
from collections import defaultdict
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:input()

"""========main code==============="""
t=1
#t=ii()
for _ in range(t):
    a,b=ml()
    if(b-a>=2019):
        print(0)
    else:
        ans=1e18
        for i in range(a,b+1):
            for j in range(i+1,b+1):
                ans=min(ans,(i*j)%2019)
        print(ans)        