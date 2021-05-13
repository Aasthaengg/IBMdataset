#頂点を見た時に，枝分かれの本数に応じてansを更新
#permutationのリストを先に作っておく

import sys
input = sys.stdin.readline

mod=10**9+7


N,K=map(int,input().split())
ab=[list(map(int, input().split())) for _ in range(N - 1)]
adj=[[] for _ in range(N)]

for a,b in ab:
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
    
    
#順列(K-2)Piを先に
P=[1]
for i in range(N):
    P.append((P[-1]*(K-2-i))%mod)
    

q=[(0,-1,0)]#node,parent,depth

ans=1
while q!=[]:
    v,p,d=q.pop()
    #深さ0or1で塗ることができる色数は異なる
    l=len(adj[v])
    if d==0:
        ans*=(K-1)
    ans*=(P[l-1])
    ans%=mod
    for i in range(l):
        next_v=adj[v][i]
        #葉は追加しない
        if next_v!=p and len(adj[next_v])!=1:
            q.append((next_v,v,d+1))
if N==1:
    ans=1
print((ans*K)%mod)