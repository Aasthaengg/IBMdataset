import collections
N,A,B=map(int,input().split())
v=list(map(int,input().split()))
v.sort(reverse=True)
l=[]
frac=[1]*51
modfrac=[1]*51
avg=0
for i in range(1,51):
    frac[i]=frac[i-1]*i
for i in range(A):
    l.append(v[i])
avg=(sum(l)/len(l))
mi=min(l)
cnt=0
c1 = collections.Counter(l)
c2 = collections.Counter(v)
if len(set(l))==1:
    n=c2[mi]
    for i in range(A,min(B+1,n+1)):
        up=1
        down=1
        for j in range(1,i+1):#nCi
            up=up*(n-i+j)
            down=down*j
        cnt=cnt+(up//down)
else:
    n=c2[mi]
    r=c1[mi]
    up=1
    down=1
    for i in range(1,r+1):
        up=up*(n+1-i)
        down=down*i
    cnt=(up//down)
print(avg)
print(cnt)