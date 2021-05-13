import heapq
X,Y,A,B,C=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
S=[]
T=[]
for i in range(X):
    heapq.heappush(S,-p[i])
for i in range(Y):
    heapq.heappush(S,-q[i])
for i in range(C):
    heapq.heappush(T,-r[i])
ans=0
for i in range(X+Y):
    if len(T)>0:
        if S[0]<T[0]:
            ans+=heapq.heappop(S)
        else:
            ans+=heapq.heappop(T)
    else:
        ans+=heapq.heappop(S)
print(-ans)
