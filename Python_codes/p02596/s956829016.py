K=int(input())
ans=-1
p=10
if K%7==0:
  l=9*K//7
else:
  l=9*K
for i in range(K):
  if p%l==1:
    ans=i+1
    break
  else:
    p=(p%l)*10
print(ans)