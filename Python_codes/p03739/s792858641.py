n=int(input())
a=list(map(int,input().split()))
#+-+-
ans=0
s=0
for i in range(n):
    f=i%2
    s+=a[i]
    if f==0:
        if s<=0:
            ans+=-s+1
            s=1
    else:
        if s>=0:
            ans+=1+s
            s=-1
#-+-+
anss=0
s=0
for i in range(n):
    f=i%2
    s+=a[i]
    if f==1:
        if s<=0:
            anss+=-s+1
            s=1
    else:
        if s>=0:
            anss+=1+s
            s=-1
print(min(ans,anss))

