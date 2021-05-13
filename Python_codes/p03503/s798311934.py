n=int(input())
f=[list(map(int,input().split())) for i in range(n)]
p=[list(map(int,input().split())) for i in range(n)]

ans=-10**18
for i in range(1<<10):
  if i==0:continue
  tp=0
  for j in range(n):
    tcnt=0
    for k in range(10):
      if i&(1<<k):tcnt+=f[j][k]
    tp+=p[j][tcnt]
  ans=max(ans,tp)
print(ans)
