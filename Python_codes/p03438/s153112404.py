n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt=[0]*n
for i in range(n):
    cnt[i]=b[i]-a[i]
cnt.sort()
p=n-1
for i in range(n):
    while cnt[i]<0:
        if cnt[p]<=1:
            print("No")
            exit()
        elif cnt[p]-abs(cnt[i])*2>=2:
            cnt[p]-=abs(cnt[i])*2
            cnt[i]=0
        elif cnt[p]-abs(cnt[i])*2>=0:
            cnt[p]-abs(cnt[i])*2
            cnt[i]=0
            p-=1
        else:
            x=cnt[p]//2
            cnt[i]+=x
            p-=1
print("Yes")
