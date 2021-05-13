import copy,heapq

N,K=map(int,input().split())
V=list(map(int,input().split()))

ans=0
left=copy.copy(V)
for i in range(1,N):
    left[i]+=left[i-1]
right=copy.copy(V)
for i in range(1,N):
    right[-i-1]+=right[-i]
for i in range(0,N+1):
    for j in range(0,N-i+1):
        dispose=K-i-j
        if 0>dispose:
            continue
        test=0
        q=[]
        if i>0:
            test+=left[i-1]
            q+=V[:i]
        if j>0:
            test+=right[-j]
            q+=V[N-j:N]

        heapq.heapify(q)
        while dispose>0 and q:
            x=heapq.heappop(q)
            if 0>x:
                test-=x
                dispose-=1
            else:
                break
        ans=max(ans,test)

print(ans)
