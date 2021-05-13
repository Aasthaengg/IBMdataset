n=int(input())
li=list(map(int, input().split()))
ans=0
m=0
ans=0
for i in range(n-1):
    if li[i]>=li[i+1]:
        m+=1
    else:
        ans=max(ans,m)
        m=0
ans=max(ans,m)
print(ans)