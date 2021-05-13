n=int(input())
k=int(input())
x=[int(i) for i in input().split()]
ans=int()
for j in range(n):
    ans+=min(x[j],abs(k-x[j]))*2
print(ans)