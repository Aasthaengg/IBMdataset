import sys
sys.setrecursionlimit(100000)

n, m=map(int, input().split())
a=[0 for i in range(m)]
b=[0 for i in range(m)]
g=[list() for i in range(1+n)]
#print(g)

par=[i for i in range(n)]
cnt_con=[1 for i in range(n)]

def root(x):
    if x==par[x]:
        return x
    else:
        par[x]=root(par[x])
        return par[x]
def connect(x,y):
    #par[x]=root(x)
    #par[y]=root(y)
    if root(x)==root(y):
        0
    else:
        cnt_con[root(y)]+=cnt_con[root(x)]
        par[root(x)]=root(y)      
    return

for i in range(m):
    a[i], b[i]=map(int, input().split())
    a[i], b[i]=a[i]-1, b[i]-1


tmp=int(n*(n-1)/2)
ans=[0]*m
ans[-1]=tmp
#ans[0]=0
#print('a,b=',a,b)
for i in range(m-1,-1,-1):
    ans[i]=tmp
    if root(a[i])==root(b[i]):
        0
    else:
        tmp-=cnt_con[root(a[i])]*cnt_con[root(b[i])]
    connect(a[i],b[i])
    #print('i,tmp',i,(a[i],b[i]),ans[i],tmp,par,cnt_con)
    

    
for i in range(m):
    print(ans[i])

