n=int(input())
nums=list(map(int,input().split()))
count=0
for i in range(n):
    minj=i
    for j in range(i,n):
        if nums[j] < nums[minj]:
            minj=j
    if not i==minj:
        v=nums[i]
        nums[i]=nums[minj]
        nums[minj]=v
        count+=1
print(*nums)
print(count)
