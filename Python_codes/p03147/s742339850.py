n,*h=map(int,open(0).read().split())
ans=0
left=0
while True:
    while left<n and h[left]==0:
        left+=1
    
    if left==n:
        break
    
    right=left

    while right+1<n and h[right+1]>0:
        right+=1
    
    ans+=1
    for i in range(left,right+1):
        h[i]-=1
    
print(ans)