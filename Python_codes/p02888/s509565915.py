import bisect
n=int(input())
l=sorted(list(map(int,input().split())))
g=0
for ai in range(n-2):
    for bi in range(ai+1,n-1):
        g+=max(0,bisect.bisect_left(l,l[bi]+l[ai])-1-bi)
print(g)
