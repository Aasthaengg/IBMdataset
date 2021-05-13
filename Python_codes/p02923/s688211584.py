n=int(input())
h=list(map(int,input().split()))
cnt=0
ans=0
for i in range(n-1):
    if h[i+1]<=h[i]:
        cnt+=1
        ans=max(ans,cnt)
    else:
        cnt=0
print(ans)