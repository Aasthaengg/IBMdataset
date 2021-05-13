from math import ceil

def check(arr,n,k,w):
    res=0
    for i in range(n):
        res+=ceil(arr[i]/w)-1
    if res<=k:
        return 1
    return 0
    
n,k=map(int,input().split())
arr=list(map(int,input().split()))

minn=1
maxx=max(arr)
while(1):
    val=ceil((minn+maxx)/2)
    if maxx==val:
        if check(arr,n,k,val) and (val==1 or not(check(arr,n,k,val-1))):
            print(val)
            break
        else:
            print(val-1)
            break
    if check(arr,n,k,val):
        maxx=val
    else:
        minn=val
    





 