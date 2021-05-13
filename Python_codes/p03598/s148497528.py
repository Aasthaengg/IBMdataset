n=int(input())
k=int(input())
x=list(map(int,input().split()))
ans=0
mid=k/2
for i in x:
    if i>mid:
        ans+=(2*abs(k-i))
    else:
        ans+=i*2
    
print(ans)