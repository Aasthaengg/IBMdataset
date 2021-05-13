n=int(input())
lst=list(map(int,input().split()))
if n%2==0:
    cnt=[0]*n
    for i in range(n):
        p=lst[i]
        if p%2==0:
            print(0)
            exit()
        cnt[p]+=1
        if cnt[p]>=3:
            print(0)
            exit()
    print(pow(2,n//2,10**9+7))
else:
    cnt=[0]*n
    for i in range(n):
        p=lst[i]
        if p%2==1:
            print(0)
            exit()
        cnt[p]+=1
        if p==0:
            if cnt[0]>=2:
                print(0)
                exit()
        else:
            if cnt[p]>=3:
                print(0)
                exit()
    print(pow(2,n//2,10**9+7))