n,W=map(int,input().split())
wv=[list(map(int,input().split())) for _ in [0]*n]
d={0:0}
for w,v in wv:
    temp=dict()
    for k,i in d.items():
        if k+w in d.keys():
            temp[k+w]=max(d[k+w],i+v)
        else:
            temp[k+w]=i+v
    d.update(temp)
    s=sorted(d.keys())
    m=-1
    for i in s:
        if d[i]<=m:
            del d[i]
        else:
            m=d[i]
print(max([v for w,v in d.items() if w<=W]+[0]))