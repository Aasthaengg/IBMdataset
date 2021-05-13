n,m,q=map(int,input().split())
def ruiseki(a):
    l=[0]
    for i in range(len(a)):
        l.append(l[i]+a[i])
    del l[0]
    return l
l=[]
def niruiseki(a):
    l.append(ruiseki(a[0]))
    for i in range(1,len(a)):
        p=[l[i-1][0]+a[i][0]]
        q=[a[i][0]]
        for j in range(1,len(a[i])):
            q.append(q[j-1]+a[i][j])
            p.append(q[j]+l[i-1][j])
        l.append(p)
ll=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    ll[a][b]+=1
niruiseki(ll)
for i in range(q):
    a,b=map(int,input().split())
    print(l[b][b]+l[a-1][a-1]-l[a-1][b]-l[b][a-1])