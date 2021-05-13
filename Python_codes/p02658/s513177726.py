n=input()
list1=list(map(int,input().split()))
if 0 in list1:
    print(0)
else:
    ans=1
    for i in list1:
        ans*=i
        if ans>1e18:
            ans=-1
            break
    print(ans)
