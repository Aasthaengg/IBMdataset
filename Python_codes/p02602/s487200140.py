n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=["No","Yes"]
for i in range(n-k):
    print(ans[a[i]<a[i+k]])