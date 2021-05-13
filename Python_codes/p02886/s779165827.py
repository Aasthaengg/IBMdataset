n=int(input())
tako=list(map(int,input().split()))
ans=0
for i in range(n-1):
    for j in range(1,n):
        if not j<=i:
            
          
            ans+=tako[i]*tako[j]
print(ans)