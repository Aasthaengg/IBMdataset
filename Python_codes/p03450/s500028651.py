n,m=map(int,input().split())
graph = [[] for i in range(n)]
x=[None for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[b-1].append([a-1, -c])
    graph[a-1].append([b-1, c])
def fuck():
    for i in range(n):
        if x[i]==None:
            x[i]=0
            q=[i]
        while q:
            j=q.pop()
            for  d, e in graph[j]:
                if x[d]==None:
                    q.append(d)
                    x[d]=x[j]+e
                elif x[d]!=x[j]+e:
                    return False
    return True
if fuck():
    print("Yes")
else:
    print("No")

