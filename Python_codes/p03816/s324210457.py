import collections
n=int(input())
a=list(map(int,input().split()))

rec=collections.Counter(a)
ans=0
for i in range(100001):
    if rec[i]>1:
        ans+=rec[i]-1
ans=-(-ans//2)*2
print(n-ans)
