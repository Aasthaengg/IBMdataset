n,k=map(int,input().split())
lst=list(map(int,input().split()))
ans=float("inf")
for i in range(n-k+1):
    left=lst[i]
    right=lst[i+k-1]
    if left==0 and right==0:
        print(0)
        exit()
    if left<0 and right<=0:
        ans=min(ans,abs(left))
    elif left<0 and right>0:
        if abs(left)>abs(right):
            ans=min(ans,abs(left)+right*2)
        else:
            ans=min(ans,abs(left)*2+right)
    else:
        ans=min(ans,right)
print(ans)