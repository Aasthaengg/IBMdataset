n=int(input())
a=[-1 for i in range(n)]
d=[[] for i in range(n)]
for i in range(n-1):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    d[u].append([v,w])
    d[v].append([u,w])
e=0
a[0]=0
l=[]
for i,j in d[0]:
    a[i]=(a[0]+j)%2
    l.append(i)
while len(l)>0:
    b=l.pop()
    for i,j in d[b]:
        if a[i]==-1:
            a[i]=(a[b]+j)%2
            l.append(i)
print(*a,sep='\n')