N=int(input())
hen={i:set([]) for i in range(1,N+1)}
for i in range(0,N-1):
    a,b=map(int,input().split())
    hen[a].add(b)
    hen[b].add(a)

parent={i:-1 for i in range(1,N+1)}
parent[1]=0
q=set([])
sub=set([])
q.add(1)
while q:
    while q:
        x=q.pop()
        for p in hen[x]:
            if parent[p]==-1:
                parent[p]=x
                sub.add(p)

        if not q:
            q=sub
            sub=set([])
            break

subtreesize={i:1 for i in range(1,N+1)}
q=set([])
for i in range(1,N+1):
    if i!=1 and len(hen[i])==1:
        q.add(i)
sub=set([])
flag={i:0 for i in range(1,N+1)}
while q:
    while q:
        x=q.pop()
        p=parent[x]
        if p!=1:
            subtreesize[p]+=subtreesize[x]
            flag[p]+=1
            if flag[p]==len(hen[p])-1:
                sub.add(p)
        else:
            subtreesize[1]+=subtreesize[x]

        if not q:
            q=sub
            sub=set([])
            break

s=N
load=[N]
while s!=1:
    s=parent[s]
    load.append(s)


depth=len(load)
white=subtreesize[load[depth//2-1]]
black=N-white
if white>=black:
    print('Snuke')
else:
    print('Fennec')