N=int(input())
arr=list(map(int,input().split()))

count=0
for i in range(N):
    if arr[i]<0:
        count+=1
        arr[i]*=-1


if count%2!=0:
    print(sum(arr)-2*min(arr))
else:
    print(sum(arr))