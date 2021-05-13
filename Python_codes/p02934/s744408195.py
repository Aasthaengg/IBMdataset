import math
from collections import defaultdict
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:(input())

"""========main code==============="""
a=ii()
n=ll()
ans=0
for i in n:
    ans+=1/i
print(1/ans)    