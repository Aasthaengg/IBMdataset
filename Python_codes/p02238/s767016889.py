from collections import deque

seen=[]
first_order =[]
last_order = []

def dfs(g, v, first_ptr, last_ptr):
    first_ptr=first_ptr+1
    last_ptr=first_ptr
    
    first_order[v] = first_ptr
    seen[v]=True 
    for next_v in g[v]:
        if seen[next_v]:
            continue
        first_ptr, last_ptr=dfs(g, next_v, first_ptr, last_ptr)
    last_ptr=last_ptr+1
    first_ptr=last_ptr

    last_order[v] = last_ptr
    return first_ptr, last_ptr

icase=1
if icase==0:
    n,m=map(int,input().split())
    g = [deque([]) for _ in range(n + 1)]
    for i in range(m):
        a,b=map(int,input().split())
        g[a].append(b)
#        g[b].append(a) # 無向グラフ
elif icase==1:        
    n=int(input())
    u=[0]*n
    k=[0]*n
#    v=[[] for i in range(n)]
    g = [deque([]) for _ in range(n + 1)]
    for i in range(n):
        ai=list(map(int,input().split()))
        u[i]=ai[0]
        k[i]=ai[1]
        g[i]=deque(ai[2:])
        for j in range(len(g[i])):
            g[i][j]-=1    
elif icase==2:
    n=6
    u=[1,2,3,4,5,6]
    k=[2,2,1,1,1,0]
    g = [deque([]) for _ in range(n + 1)]

    g[0]=deque([1,2])
    g[1]=deque([2,3])
    g[2]=deque([4])
    g[3]=deque([5])
    g[4]=deque([5])
    g[5]=deque([])
    g[5]=deque()

seen=[False]*n
first_ptr=0
last_ptr=0
first_order =[-1]*n
last_order = [-1]*n

for v in range(n):
    if seen[v]:
        continue
    else:
        first_ptr, last_ptr=dfs(g,v,first_ptr, last_ptr)

for v in range(n):
    print(v+1,first_order[v],last_order[v]) 
    
