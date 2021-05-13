from collections import deque
N,Q = map(int, input().split())
a = [0] * (N-1)
b = [0] * (N-1)
g=[[] for i in range(N+1)]
for i in range(N-1):
    a[i], b[i] = map(int, input().split())
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])
p = [0] * Q
x = [0] * Q
ans=[0]*(N+1)
for i in range(Q):
    p[i], x[i] = map(int, input().split())
    ans[p[i]]+=x[i]
    
q = deque([1]) 
ch=[0]*(N+1)
while len(q) > 0:
    pp = q.popleft()     # キュー取りだし（先頭）
    if ch[pp]==0:
        ch[pp]=1
    for u in g[pp]:
        if ch[u]!=1:
           
            ans[u]+=ans[pp]
            q.append(u)
    #print(pp,l,q)

    
for i in range(1,N+1):
    print(ans[i],end=' ')