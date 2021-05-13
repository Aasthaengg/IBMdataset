n=int(input())
a=list(map(int,input().split()))
ans=0
right=0
np=a[0]
nx=a[0]
for i in range(n):
    left=i
    if i!=0:
        np-=a[left-1]
        nx^=a[left-1]
    while np==nx:
        right+=1
        if right==n:
            break
        np+=a[right]
        nx^=a[right]
    else:
        np-=a[right]
        nx^=a[right]
    right-=1
    ans+=(right-left+1)
print(ans)