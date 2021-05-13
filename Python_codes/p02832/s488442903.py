n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
c=1
for i in range(n):
  if a[i]==c:
    ans[i]=1
    c+=1
if sum(ans)==0:
  print(-1)
else:
  print(n-sum(ans))