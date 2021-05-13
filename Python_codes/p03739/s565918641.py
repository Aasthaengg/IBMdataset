n=int(input())
a=list(map(int,input().split()))

#i%2==0 の時+
cnt=0
sums=0

for i in range(n):
    if i%2==0:
        if sums+a[i]<=0:
            tmp=abs(sums+a[i])+1
            sums=1
            cnt+=tmp
        else:
            sums+=a[i]
            tmp=a[i]
    else:
        #マイナスになってほしい
        if sums+a[i]>=0:
            tmp=abs(sums+a[i])+1
            sums=-1
            cnt+=tmp
        else:
            sums+=a[i]
            tmp=a[i]
    #print(a[i],tmp)

ans=cnt
#print("##############")
#i%2==0 の時+
cnt=0
sums=0

for i in range(n):
    if i%2==1:
        if sums+a[i]<=0:
            tmp=abs(sums+a[i])+1
            sums=1
            cnt+=tmp
        else:
            tmp=a[i]
            sums+=a[i]
    else:
        #マイナスになってほしい
        if sums+a[i]>=0:
            tmp=abs(sums+a[i])+1
            sums=-1
            cnt+=tmp
        else:
            tmp=a[i]
            sums+=a[i]
    #print(a[i],tmp)

print(min(cnt,ans))





