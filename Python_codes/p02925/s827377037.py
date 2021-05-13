def main():
    from collections import defaultdict,deque
    from itertools import count
    (n,),*a=[list(map(int,t.split()))for t in open(0)]
    d=defaultdict(count().__next__)
    es=[]
    for i,b in enumerate(a,1):
        for j,k in zip(b,b[1:]):
            x,y=i,j
            if y<x:x,y=y,x
            v,w=i,k
            if w<v:v,w=w,v
            es+=(d[x*n+y],d[v*n+w]),
    s=len(d)
    outs=[[]for _ in range(s)]
    ins=[0]*s
    f=set(range(s))
    for i,j in es:
        outs[i]+=j,
        f-={j}
        ins[j]+=1
    q=deque(f)
    l=0
    data=[0]*s
    m=0
    while q:
        i=q.popleft()
        l+=1
        t=data[i]+1
        if t>m:m=t
        for j in outs[i]:
            ins[j]-=1
            if ins[j]<1:q+=j,
            if t>data[j]:data[j]=t
    print(-(l<s)or m)
main()