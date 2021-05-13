N,M=map(int,input().split())
S=input()

load=[S[-i-1] for i in range(0,N+1)]


near=[-1 for i in range(0,N+1)]
log=0
for i in range(0,N+1):
    if load[i]=='0':
        near[i]=i
        log=i
    else:
        near[i]=log

ans=[]
start=0
while start<N:
    if N>start+M:
        next=near[start+M]
        if start>=next:
            print(-1)
            break
        ans.append(next-start)
        start=next
    else:
        ans.append(N-start)
        start=N
else:
    ans=ans[::-1]
    print(*ans)
