n=int(input())
p=list(map(int,input().split()))

data=n+1
ans=0
for i in range(n):
  if data>p[i]:
    data=p[i]
    ans+=1
print(ans)