n,x=map(int, input().split())
l=list( map(int, input().split()))
a=0
ans=1
for i in range(n):
    a=a+l[i]
    if a<=x:
        ans=ans+1
print(ans)