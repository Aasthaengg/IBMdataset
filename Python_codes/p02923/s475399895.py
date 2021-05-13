N=int(input())
H=list(map(int,input().split()))

ans=0
temp=0
for i in range(N-1):
    if H[i]<H[i+1]:
        temp=0
    else:
        temp+=1
    ans=max(ans,temp)

print(ans)