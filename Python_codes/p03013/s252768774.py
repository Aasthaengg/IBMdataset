n,m=map(int,input().split())
a=[int(input()) for _ in range(m)]
l=[1]+[0 for _ in range(n+5)]
if m==0:a=[200000]
for x in range(n):
    if x<a[0]:
        l[x+1]+=l[x]
        l[x+2]+=l[x]
    if x==a[0]:
        if len(a)>=2:a.pop(0)
        else:a[0]=200000
print(l[n]%(10**9+7))