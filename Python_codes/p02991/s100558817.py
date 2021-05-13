from collections import deque
n,m=map(int,input().split())
g=[[] for i in range(3*n)]
for i in range(m):
    a,b=map(int,input().split())
    g[3*(a-1)].append(3*(b-1)+1)
    g[3*(a-1)+1].append(3*(b-1)+2)
    g[3*(a-1)+2].append(3*(b-1))
s,t=map(int,input().split())
s-=1
t-=1
s*=3
t*=3
q=deque([[s,0]])
v=[0]*(3*n)
while q:
    p=q.popleft()
    v[p[0]]=1
    for j3 in g[p[0]]:
        if j3==t:
            print((p[1]+1)//3)
            exit()
        if v[j3]==0:
            v[j3]=1
            q.append([j3,p[1]+1])
print(-1)
