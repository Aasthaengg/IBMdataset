n=int(input())
p=list(map(int,input().split()))
Min=p[0]
ans=1
for i in range(1,n):
  if p[i]<=Min:
    ans +=1
    Min=p[i]
print(ans)