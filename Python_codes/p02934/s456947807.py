N=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(N):
    a[i]=1/a[i]

for j in range(N):
    ans+=a[j]

print(1/ans)
