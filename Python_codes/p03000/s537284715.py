n,x=map(int,input().split())
L=list(map(int,input().split()))
p,ans=0,1
for i in range(n):
    if p+L[i]<=x:
        p+=L[i]
        ans+=1
    else:
        break
print(ans)