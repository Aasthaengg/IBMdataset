#n=int(input())
#n,m=list(map(int,input().split()))
#a=list(map(int,input().split()))
input_list = lambda : list(map(int,input().split()))

from collections import Counter 
from collections import defaultdict
import itertools
import sys
sys.setrecursionlimit(10**6)

def sol(num,w,node,ans):
    now=node[num]
    
    for each in now:
        ne_n=each[0]
        ne_w=each[1]
        if ans[ne_n]!=-1:
            continue
        if ne_w==0:
            ans[ne_n]=ans[num]
        else:
            ans[ne_n]=1-ans[num]
        
        sol(ne_n,ne_w,node,ans)




n=int(input())
node=[[] for _ in range(n)]
for _ in range(n-1):
    u,v,w=input_list()
    w=w%2
    u-=1
    v-=1
    node[u].append([v,w])
    node[v].append([u,w])

ans=[-1 for _ in range(n)]
ans[0]=0
sol(0,0,node,ans)
for i in ans:
    print(i)