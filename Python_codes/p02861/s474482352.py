import sys
input=sys.stdin.readline
import math
from collections import defaultdict,deque
from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

t=ii()
lol=[]
for i in range(t):
    a,b=ml()
    lol.append([a,b])
yo=0    
cnt=0
for i in list(permutations(lol)):
    for j in range(1,len(i)):
        x=i[j][0]-i[j-1][0]
        y=i[j][1]-i[j-1][1]
        yo+=math.sqrt(x*x+y*y)
    cnt+=1
print(yo/cnt)    