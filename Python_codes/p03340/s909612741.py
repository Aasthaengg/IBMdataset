n=int(input())
a=list(map(int,input().split()))
ans=0
j=0
b=0
for  i in range(n):
    while j<n and b^a[j]==b+a[j]:
        b^=a[j]
        j+=1
    ans+=j-i    
    b^=a[i]
print(ans)