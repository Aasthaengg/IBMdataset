import itertools
n,k=map(int,input().split())
l=list(map(int,input().split()))
if k>42:
    l=[n]*n
    print(*l)
else:
    for _ in range(k):
        countl=[0]*(n+1)
        for i in range(n):
            countl[max(1,i+1-l[i])]+=1
            if i+2+l[i]<=n:
                countl[i+2+l[i]]-=1
            
        l=list(itertools.accumulate(countl))
        l.remove(l[0])
    print(*l)