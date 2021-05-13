n=int(input())
a=list(map(int,input().split()))
if 0 in a:
    ans=0
    for i in range(n):
        ans+=abs(a[i])
    print(ans)
else:
    num=0
    for i in range(n):
        if a[i]<0:
            num+=1
        a[i]=abs(a[i])
    if num%2==0:
        print(sum(a))
    else:
        print(sum(a)-(min(a)*2))
