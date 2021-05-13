MAX=100000
def Allocate(A, p, k, n):
    count=1
    s=0     
    index=0
    while index<n:
        if s+A[index]<=p:
            s+=A[index]
            index+=1
        else:
            count+=1
            s=0
        if count>k:
            return False

    return True
         
    
n, k=map(int,input().split())
A=[int(input()) for i in range(n)]
left=0
right=MAX*MAX
while left+1<right:
    mid=left+(right-left)//2
    if Allocate(A,mid,k,n):
        right=mid
    else:
        left=mid
print(right)
