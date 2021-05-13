import collections
n=int(input())
a=list(map(int,input().split()))
c=collections.Counter(a)
cnt=0
for a in c:
    if c[a]-a>=0:
        cnt+=min(c[a]-a,c[a])
    else:
        cnt+=c[a]
print(cnt)
        
