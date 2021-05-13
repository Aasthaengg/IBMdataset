n=int(input())
arr1=list(map(int,input().split()))
arr2=arr1[:]
ans1=0
ans2=0

if arr1[0]<=0:
    ans1+=abs(arr1[0])+1
    arr1[0]=1
if arr2[0]>=0:
    ans2+=arr2[0]+1
    arr2[0]=-1

sum1=arr1[0]
for i in range(1,n):
    tmp=sum1+arr1[i]
    if i%2==1:
        if tmp>=0:
            ans1+=tmp+1
            sum1=-1
        else:
            sum1=tmp
    else:
        if tmp<=0:
            ans1+=abs(tmp)+1
            sum1=1
        else:
            sum1=tmp
sum2=arr2[0]
for i in range(1,n):
    tmp=sum2+arr2[i]
    if i%2==0:
        if tmp>=0:
            ans2+=tmp+1
            sum2=-1
        else:
            sum2=tmp
    else:
        if tmp<=0:
            ans2+=abs(tmp)+1
            sum2=1
        else:
            sum2=tmp
print(min(ans1,ans2))