import bisect
n=int(input())
s=list(input())
a={chr(i):[] for i in range(97,123)}
for i,c in enumerate(s):
    bisect.insort(a[c],i+1)
for i in range(int(input())):
    p,q,r=list(map(str,input().split()))
    if p=="1":
        q=int(q)
        b=s[q-1]
        if b!=r:
            a[b].pop(bisect.bisect_left(a[b],q))
            bisect.insort(a[r],q)
            s[q-1]=r
    else:
        d=0
        for l in a.values():
            g=bisect.bisect_left(l,int(q))
            if g<len(l) and l[g]<=int(r):
                d+=1
        print(d)