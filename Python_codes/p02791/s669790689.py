n=int(input())
p=list(map(int,input().split()))
ans=0
m=10**10
for i in range(n):
  if m>=p[i]:
    ans+=1
    m=p[i]

print(ans)