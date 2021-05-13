n=int(input())
arr=[0]*n
for i in range(n):
    arr[i]=int(input())

arr=sorted(arr)
num=arr[0]
tmp=1
ans=0
for i in range(1,n):
    if arr[i]==num:
        tmp+=1
    else:
        if tmp%2==1:
            ans+=1
        num=arr[i]
        tmp=1
if tmp%2==1:
    ans+=1    
print(ans)