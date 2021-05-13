n,q=map(int,input().split())
L=[[] for i in range(n+1)]
S=[0 for i in range(n+1)]
V=[0 for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    L[a].append(b)   
    L[b].append(a)

for _ in range(q):
    p,x=map(int,input().split())
    S[p]+=x


que=[1]
head=0
V[1]=1
while len(que)>head:
    now=que[head]
    head+=1
    for nex in L[now]:
        if V[nex]==0:
            V[nex]=1
            que.append(nex)
            S[nex]+=S[now]

print(" ".join([str(i) for i in S[1:]]))