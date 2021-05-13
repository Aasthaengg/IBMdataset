n=int(input())
a=list(map(int,input().split()))
b=[0,0,0]
ans=1
mod=1000000007
for i in range(n):
    aa=a[i]
    tmp=0
    flg=False
    for j in range(3):
        if aa==b[j]:
            tmp+=1
            if flg==False:
                b[j]+=1
                flg=True
    ans*=tmp
    ans%=mod
print(ans)