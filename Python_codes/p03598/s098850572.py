n=int(input())
k=int(input())
x=list(map(int,input().split()))
ans=0
for i in range(n):
    tmp=2*min(abs(x[i]-0),abs(x[i]-k))
    ans+=tmp
print(ans)