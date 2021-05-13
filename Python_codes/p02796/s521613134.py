n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
b=[[a[i][0]+a[i][1],a[i][0]-a[i][1]] for i in range(n)]
b.sort()
ans=1
tmp=b[0][0]
for i in range(n):
  if tmp<=b[i][1]:
    ans+=1
    tmp=b[i][0]
print(ans)