def resolve():
    mod=1e9+7
    n=int(input())
    a=list(map(int,input().split()))
    ans=1
    cnt=[0]*(n+1)
    cnt[0]=3
    for i in range(n):
        if cnt[a[i]]>0:
            ans=(ans*cnt[a[i]])%mod
            cnt[a[i]]-=1
            cnt[a[i]+1]+=1
        else :
            ans=0
    print(int(ans))
resolve()