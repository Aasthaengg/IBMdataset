import sys
from collections import deque
from collections import defaultdict
from collections import Counter

def conn(n,m,e):
    d=dict(zip(range(1,n+1),range(-1,(-1)*n-1,-1)))
    td=defaultdict(lambda:deque([])) #tdは同値類がキーで中の元が値
    c=1
    for edge in e:
        a=edge[0]
        b=edge[1]
        da=d[a] #da,dbはa,bの含まれる同値流のラベル
        db=d[b]
        if da<0 and db<0:
            d[a]=c
            d[b]=c
            td[c].append(a)
            td[c].append(b)
            c+=1
        elif da>0 and db<0:
            d[b]=da
            td[d[a]].append(b)
        elif da<0 and db>0:
            d[a]=db
            td[d[b]].append(a)
        elif da>0 and db>0 and da!=db:
            for x in td[db]:
                d[x]=da
                td[da].append(x)

    return list(d.values())

def main(n,k,l,e1,e2):
    d1=conn(n,k,e1)
    d2=conn(n,l,e2)
    p=tuple(zip(iter(d1),iter(d2)))
    d=Counter(p)
    # print(d1,d2,d,p)
    d[(k,l)]=1
    print(' '.join([str(d[x]) for x in p]))

if __name__=='__main__':
    ssr=sys.stdin.readline
    n,k,l=map(int,ssr().strip().split())
    e1=[]
    e2=[]
    for _ in range(k):
        e1.append(tuple(map(int,ssr().strip().split())))
    for _ in range(l):
        e2.append(tuple(map(int,ssr().strip().split())))
    main(n,k,l,e1,e2)
