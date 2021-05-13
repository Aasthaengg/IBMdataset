import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
pair=[i for i in range(n)]
a=[0]*m
b=[0]*m
for i in range(m):
    ai,bi=map(int,input().split())
    a[i]=ai-1
    b[i]=bi-1
    
def root(x):
    if x==pair[x]:
        return x
    else:
        tmp=root(pair[x])
        pair[x]=tmp
        return tmp

def unite(x,y):
    x=root(x)
    y=root(y)
    if x==y:return
    pair[x]=y

icnt=0
for i in range(m):
    pair=[i for i in range(n)]
    for ii in range(m):
        if ii==i:
            continue
        unite(a[ii],b[ii])

    l=[root(ii) for ii in range(n)]
#    print(i,l)
    lenpair=len(set(l))    
    if lenpair!=1:
        icnt+=1

print(icnt)