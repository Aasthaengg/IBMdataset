n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    b=a[i]
    c=a[b-1]
    if i+1==c:
        ans+=1
ans//=2
print(ans)
