import sys,heapq

mod = 10**9+7 #出力の制限
N = 2*10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N,K=map(int,input().split())
hen={i:[] for i in range(1,N+1)}
for i in range(0,N-1):
    a,b=map(int,input().split())
    hen[a].append(b)
    hen[b].append(a)

parent={i:-1 for i in range(1,N+1)}
parent[1]=0
q=[1]
heapq.heapify(q)
sub=[]
heapq.heapify(sub)
while q:
    while q:
        x=heapq.heappop(q)
        for p in hen[x]:
            if parent[p]==-1:
                parent[p]=x
                heapq.heappush(sub,p)
        #何らかの操作
        #ここでsubキューに次に使うものを格納
        if q==[]:
            q=sub
            sub=[]
            heapq.heapify(sub)
            break

ans={i:1 for i in range(1,N+1)}
flag={i:0 for i in range(1,N+1)}
q=[]
for i in range(1,N+1):
    if i!=1 and len(hen[i])==1:
        q.append(i)
sub=[]
heapq.heapify(sub)
while q:
    while q:
        x=heapq.heappop(q)
        p=parent[x]
        if p!=1:
            if len(hen[p])-1>K-2:
                ans[p]=0
            else:
                ans[p]=(ans[p]*ans[x])%mod
            flag[p]+=1
            if flag[p]==len(hen[p])-1:
                ans[p]=(ans[p]*g1[K-2]*g2[K-2-flag[p]])%mod
                heapq.heappush(sub,p)
        #何らかの操作
        #ここでsubキューに次に使うものを格納
        if q==[]:
            q=sub
            sub=[]
            heapq.heapify(sub)
            break

if len(hen[1])>K-1:
    print(0)
else:
    for i in hen[1]:
        ans[1]=(ans[1]*ans[i])%mod
    ans[1]=(ans[1]*g1[K]*g2[K-1-len(hen[1])])%mod
    print(ans[1])