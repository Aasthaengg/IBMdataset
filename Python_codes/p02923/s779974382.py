n=int(input())
a=list(map(int,input().split()))
ans=0
i=0
while i<=n-2:
  j=0
  while i+j<=n-2:
    if a[i+j]>=a[i+j+1]:
      j+=1
    else:
      break
  i+=j+1
  if j>ans:
    ans=j
print(ans)