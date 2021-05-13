N=int(input())
a=sorted(map(int,input().split()))
ans=0
left=0;right=3*N-1
for i in range(N):
    mid=right-1
    ans+=a[mid]
    right=mid-1
    left+=1
print(ans)