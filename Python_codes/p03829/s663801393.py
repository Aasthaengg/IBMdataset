n,a,b=[int(j) for j in input().split()]
x=[int(j) for j in input().split()]
ans=0
for i in range(n-1):
    ans+=min((x[i+1]-x[i])*a,b)
print(ans)