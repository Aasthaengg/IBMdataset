n=int(input())
p=list(map(int,input().split()))
ans=0
for x in range(n-2):
  if (p[x]>=p[x+1] and p[x+1]>=p[x+2]) or (p[x]<=p[x+1] and p[x+1]<=p[x+2]):
    ans+=1
print(ans)