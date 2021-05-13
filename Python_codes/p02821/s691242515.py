import bisect

n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
s=[0 for _ in range(n+1)]
for i in range(n):
    s[i+1]=s[i]+a[i]

def calc(x):
    tot=0
    num=0
    for i in range(n):
        j=bisect.bisect_left(a, x-a[i])
        num+=n-j
        tot+=s[n]-s[j]
        tot+=a[i]*(n-j)
    return [tot, num]

l=0
r=(10**5)*2+5
while l+1<r:
    c=(l+r)//2
    if calc(c)[1]>=m:
        l=c
    else:
        r=c
p=calc(l)
ans=p[0]
ans-=(p[1]-m)*l
print(ans)