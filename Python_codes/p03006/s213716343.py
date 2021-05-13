N=int(input())
s=[list(map(int, input().split())) for i in range(N)]
d={}
for i in range(N-1):
    for j in range(i+1,N):
        a=s[i]
        b=s[j]
        t=(a[0]-b[0],a[1]-b[1])
        if t in d:
            d[t]+=1
        else:
            d[t]=1
        t=(b[0]-a[0],b[1]-a[1])
        if t in d:
            d[t]+=1
        else:
            d[t]=1
m=0
for i in d.values():
    if i>m:
        m=i
print(N-m)