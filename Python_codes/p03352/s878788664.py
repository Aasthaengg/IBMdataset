x=int(input())
ans=1
for b in range(2,50):
    n=b*b
    while n<=x:
        ans=max(ans,n)
        n*=b
print(ans)