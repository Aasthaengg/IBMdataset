n=int(input())
a=[int(j)for j in input().split()]
ans=0
for i,j in enumerate(a,1):
    if i==a[j-1]:
        ans+=1
print(ans//2)