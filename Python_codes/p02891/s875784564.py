s = list(input())
k = int(input())
n=len(s)
if n!=1:
    cnt=[]
    tmp=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            tmp+=1
        else:
            cnt.append((s[i-1], tmp))
            tmp=1
        if i==n-1:
            cnt.append((s[i], tmp))

    ans=0
    if len(cnt)==1:
        ans=cnt[0][1]*k//2
    elif cnt[0][0]!=cnt[-1][0]:
        for x,y in cnt:
            ans+=y//2
        ans*=k
    else:
        for x,y in cnt:
            ans+=y//2
        ans*=k
        if (cnt[0][1]+cnt[-1][1])%2==0:
            ans+=k-1
    print(ans)

else:
    print(k//2)