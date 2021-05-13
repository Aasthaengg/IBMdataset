n,m=map(int,input().split())
t=[[0 for i in range(n)] for j in range(n)]
A,B=[],[]
for _ in range(m):
    a,b=map(int,input().split())
    A.append(a-1)
    B.append(b-1)
    t[a-1][b-1]=1
    t[b-1][a-1]=1
ans=0
for i in range(m):
    t[A[i]][B[i]]=0
    t[B[i]][A[i]]=0
    
    q=[0]
    visited={0}
    while q:
        temp=q.pop()
        for j in range(n):
            if j not in visited and t[temp][j]==1:
                q.append(j)
                visited.add(j)
    if len(visited)!=n: ans+=1
    t[A[i]][B[i]]=1
    t[B[i]][A[i]]=1
print(ans)