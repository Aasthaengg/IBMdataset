import itertools
n=int(input())
a=list(map(int,input().split()))

c=itertools.groupby(a)

ans=0
for i,gr in c:
    ans+=len(list(gr))//2
print(ans)
