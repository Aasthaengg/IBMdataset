n,k=map(int,input().split())
h=[int(input()) for i in range(n)]
a=sorted(h)
ans=a[k-1]-a[0]
for i in range(1,n-k+1):
    if a[k+i-1]-a[i]<ans:
        ans=a[k+i-1]-a[i]
print(ans)