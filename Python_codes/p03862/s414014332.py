n,x=map(int,input().split())
a=list(map(int,input().split()))

cnt=0
for i in range(1,n):
    v = a[i]+a[i-1]-x
    if v>0:
        cnt+=v
        if a[i]>=v:
            a[i]-=v
        else:
            v-=a[i]
            a[i]=0
            a[i-1]-=v
        
print(cnt)
