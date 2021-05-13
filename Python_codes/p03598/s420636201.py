n=int(input())
k=int(input())
X=list(map(int,input().split()))
ans=0
for x in X:
    ans+=min(2*abs(k-x),2*x)
print(ans)