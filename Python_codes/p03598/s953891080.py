n=int(input())
k=int(input())
x=list(map(int,input().split()))
ans=0
for i in range (n):
    if abs(x[i])>abs(x[i]-k):
	    ans+=abs(x[i]-k)*2
    else:
        ans+=x[i]*2
print(ans)