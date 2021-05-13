a,b=map(int,input().split())
ans=0
for nums in range(a,b+1):
    temp=str(nums)
    for j in range(len(temp)//2):
        if temp[j]!=temp[len(temp)-1-j]:
            break
        elif j==len(temp)//2-1:
            ans+=1

print(ans)