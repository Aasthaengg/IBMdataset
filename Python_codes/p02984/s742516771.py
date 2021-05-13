N=int(input())
A=list(map(int,input().split()))


low=0
high=10**10

#binary search the value of rain onto Mountain1
while low<=high:
    mid=(low+high)//2

    cur=mid
    for i,a in enumerate(A):
        cur=a-cur
        if cur<0:#途中で足りなくなったら、midが大きすぎ
            break
       #break
    if cur>=mid:
        low=mid+1
    else:
        if i%2==0:
            high=mid-1
        else:
            low=mid+1


ans=[]
cur=high
for a in A:
    ans.append(cur*2)
    cur=a-cur
print(" ".join(map(str,ans)))

