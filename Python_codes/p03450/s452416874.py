import sys
input = sys.stdin.readline


N,M=map(int,input().split())
adj=[[] for _ in range(N)]
inf = 10**9+1
x=[inf]*N

L=[0]*M
R=[0]*M
D=[0]*M
fro=[0]*N#何個入ってくる？

for i in range(M):
    L[i],R[i],D[i]=map(int,input().split())
    L[i]-=1
    R[i]-=1
    adj[L[i]].append([R[i],D[i]])
    fro[R[i]]+=1
    #adj[R[i]].append([L[i],-1*D[i]])
    
    
roots=[]
for i in range(N):
    if fro[i]==0:
        roots.append(i)

queue=[]
#距離の設定
for root in roots:
    if x[root]==inf:
        queue.append([root,-1])#node,pare
        x[root]=0
        while queue:
            node,par=queue.pop()
            num=len(adj[node])
            for i in range(num):
                to,cost=adj[node][i]
                if x[to]==inf:#見たことがなければ
                    x[to]=x[node]+cost
                    queue.append([to,node])
            
    
f=1
#判定
for i in range(M):
    d=x[R[i]]-x[L[i]]
    if d!=D[i]:
        f=0
            
    
    
            
            
            
if f==1:
    print("Yes")
else:
    print("No")
        
    


