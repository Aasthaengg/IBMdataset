n=int(input())
ans=0
for i in range(4):
  if int(n%10)==2:
    ans+=1
  n=n/10
print(ans)
