n=int(input())
p=list(map(int,input().split()))

l=-1
arr=[]
for i in range(n):
    if p[i]==i+1:
        arr.append(i)
ans=len(arr)
i=0
while i<len(arr)-1:
    if arr[i+1]==arr[i]+1:
        ans-=1
        i+=1
    i+=1
print(ans)