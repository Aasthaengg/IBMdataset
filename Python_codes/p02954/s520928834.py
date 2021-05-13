#krishrawat

import math
from collections import defaultdict,deque
from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

s=ip()
s.append('R')
n=len(s)
cnt=1
idx=-1
for i in range(1,n):
    if(s[i]!=s[i-1] and s[i]=='R'):
        mx=max(cnt-k,k)
        s[idx]=math.ceil(cnt/2)
        s[idx-1]=math.floor(cnt/2)
        if(k>cnt-k):
            s[idx],s[idx-1]=s[idx-1],s[idx]
        if(mx%2==0):
            s[idx],s[idx-1]=s[idx-1],s[idx]
        cnt=1
    elif(s[i]!=s[i-1] and s[i]=='L'):
        k=cnt
        idx=i
        cnt+=1
    else:
        cnt+=1
    if(s[i-1]=='L' or s[i-1]=='R'):    
        s[i-1]=0    
print(*s[:n-1])        