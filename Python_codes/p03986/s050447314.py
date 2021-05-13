x=input()
n=len(x)

for i in range(n):
    if x[i]=='S':
        left=i
        break
else:
    print(n)
    exit(0)

right=left+1
ans=n

while True:

    while right<n and x[right]=='S':
        right+=1
    
    if right>=n:
        break

    ans-=2
    right+=1
    left+=1
    while left<n and x[left]=='T':
        left+=1
    
    if left>=n:
        break

    right=max(left+1,right)


print(ans)
