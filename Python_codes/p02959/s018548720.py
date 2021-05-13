n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(len(a)-1):
    #左倒す
    left=min(a[i],b[i])
    ans+=left
    a[i]-=left
    b[i]-=left

    #
    right =min(a[i+1],b[i])
    ans+=right
    a[i+1]-=right
    b[i]-=right
print(ans)