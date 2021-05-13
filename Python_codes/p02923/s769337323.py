import math
from collections import defaultdict,deque
#from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

n=ii()
a=ll()
ans=0
cnt=0
for i in range(1,n):
    if a[i]<=a[i-1]:
        cnt+=1
        ans=max(ans,cnt)
    else:
        cnt=0
print(ans)        