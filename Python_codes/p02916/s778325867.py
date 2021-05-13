n = int(input())

a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))

memory=-1
add=0
ans=0

for i in range(n):
    ans+=b[a[i]-1]
    if a[i]==memory+1:
        ans+=add
    
    memory=a[i]
    if a[i]!=n:
        add=c[a[i]-1]
    else:
        add=0

print(ans)