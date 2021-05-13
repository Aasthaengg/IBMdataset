n,k=map(int,input().split())
arr=list(map(int,input().split()))
def isvalid(mid,k):
    if mid==0:
        return False
    ans=k
    for i in arr:
        if i>mid:
            ans-=i//mid
    return ans>=0


l=0
r=10**9
while(l<r):
    mid=(l+r)//2
    if isvalid(mid,k):
        r=mid
    else:
        l=mid+1
print(l)











