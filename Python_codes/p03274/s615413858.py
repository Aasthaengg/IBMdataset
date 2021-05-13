n,k=map(int,input().split())
*x,=map(int,input().split())

ans=10**10

for i in range(n-k+1):
    left=x[i]
    right=x[i+k-1]

    if left*right>=0:
        ans=min(ans,max(abs(left),abs(right)))
    else:
        ans=min(ans,right-left+min(abs(right),abs(left)))

print(ans)