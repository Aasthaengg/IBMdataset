n=int(input())
a=list(map(int,input().split()))
import collections
l=collections.Counter(a)
q=int(input())
s=sum(a)
for i in range(q):
    b,c=map(int,input().split())
    s+=(c-b)*l[b]
    l[c]+=l[b]
    l[b]=0
    print(s)