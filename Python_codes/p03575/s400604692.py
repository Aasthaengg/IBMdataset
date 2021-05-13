n,m=map(int,input().split())

visit=[0 for i in range(n)]
side=[[False for i in range(n)] for j in range(n)]

l=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    side[a-1][b-1]=True
    side[b-1][a-1]=True
    l[a-1].append(b-1)
    l[b-1].append(a-1)

def bfs(x,y):
    que=[0]
    visit=[0 for i in range(n)]
    done=[[0 for i in range(n)] for j in range(n)]
    visit[0]=1
    while(que):
        now=que.pop(0)
    
        for i in l[now]:
            if ((now==x and i==y) or (now==y and i==x)) or (done[now][i]==True or done[i][now]==True):
                continue
            else:
                que.append(i)
                done[now][i]=True
                visit[now]+=1
                visit[i]+=1

    flag=0

    for i in visit:
        if i!=0:
            continue                  
        else:
            flag=1
            break

    if flag==1:
        return 1
    else:
        return 0

ans=0
for i in range(n):
    for j in range(i+1,n):
        if side[i][j]==True:
            ans+=bfs(i,j)

print(ans)