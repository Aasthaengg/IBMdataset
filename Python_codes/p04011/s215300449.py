import math
from collections import defaultdict
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:input()

"""========main code==============="""

t=ii()
x=ii()
y=ii()
z=ii()
k=min(t,x)
print(k*y+(t-k)*z)