n=int(input())
G=[]
for i in range(n):
    u,k,*l=map(int,input().split())
    G.append(l)
#print(G)
log_finish=[0]*n
log_start=[0]*n

from collections import deque
def dfs(G):
    q=deque()
    for i in range(n,0,-1):
        q.append((i,-1,0))
    log_finish[0]=1
    log_start[0]=1
    cnt=0
    while q:
        #print(q,cnt)
        V,P,S=q.pop()
        if log_finish[V-1]==0 or log_finish[V-1]==log_start[V-1]:
            cnt+=1
            if not log_finish[V-1]:log_start[V-1]=cnt
            log_finish[V-1]=cnt
        #print(V,P,S,cnt)


        if S==0:
            #下に遷移していくときの処理
            q.append((V,P,1))
            l=[]
            if not G[V-1]:continue
            for new_v in G[V-1]:
                if log_start[new_v-1]!=0:continue
                l.append((new_v,V,0))
            q+=l[::-1]

dfs(G)
for i in range(n):
    print(i+1,log_start[i],log_finish[i])
