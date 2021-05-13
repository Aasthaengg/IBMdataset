n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(1,n-1):
    L=[l[i-1],l[i],l[i+1]]
    if max(L)>l[i] and min(L)<l[i]:
        ans+=1
print(ans)