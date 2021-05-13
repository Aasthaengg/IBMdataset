a=list(map(int,input().split()))
a.sort()
cnt=0
if a[1]!=a[2]:
    cnt=a[2]-a[1]
    a[0]+=cnt
    a[1]+=cnt
if 1==(a[1]-a[0])%2:
    a[1]+=1
    a[2]+=1
    cnt+=1
if a[0]!=a[1]:
    n=int((a[1]-a[0])/2)
    cnt+=n
    #a[0]+=(n*2)
print(cnt)