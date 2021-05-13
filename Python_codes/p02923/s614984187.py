n=int(input())
h=list(map(int,input().split()))

ans=cnt=0
i=0
while True:
    if i==n-1:
        ans=max(ans,cnt)
        break
    if h[i]>=h[i+1]:
        cnt+=1
    else:
        ans=max(ans,cnt)
        cnt=0
    i+=1

print(ans)
