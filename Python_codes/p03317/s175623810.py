n,k=list(map(int, input().split()))
a= list(map(int, input().split()))
final=min(a)
ans=0
flag=-1
check=0
for v in a:
    if flag==-1 and v!=final:
        flag=2
        ans+=1
        check=0
        if flag==k:
            flag=-1
    elif flag>=0:
        if check==0 and v==final:
            flag-=1
            check=1
        flag+=1
        if flag==k:
            flag=-1
print(ans)