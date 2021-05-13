n=int(input())
p=[int(x) for x in input().split()]
a=n+1
ans=0
for i in range(n):
  if a>=p[i]:
    ans+=1
  a=min(a,p[i])
print(ans)