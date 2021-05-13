N,K=list(map(int,input().split()))
g=[[] for _ in range(N+1)]

mod=10**9+7

for _ in range(N-1):
    a,b=list(map(int,input().split()))
    g[a].append(b)
    g[b].append(a)

visit=[-1]*(N+1)
visit[0]=K

stack=[(0,1,0)]
ans=1


while len(stack)>0:
    parent,current,depth=stack.pop()

    ans*=visit[parent]
    ans%=mod

    if ans==0:
        break

    visit[parent]-=1

    visit[current]=K-min(2,depth+1)
    
    for child in g[current]:
        if visit[child]>-1:
            continue

        stack.append([current,child,depth+1])

print(ans)