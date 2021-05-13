from collections import defaultdict

n=int(input())
a=list(input())
b=list(input())
c=list(input())

ans=0
for i in range(n):
    d=defaultdict(int)
    d[a[i]]+=1
    d[b[i]]+=1
    d[c[i]]+=1
    ans+=3-max(d.values())
print(ans)
