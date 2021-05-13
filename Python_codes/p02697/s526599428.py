n,k=map(int,input().split())
ans=[[] for _ in range(n//2)]
if n%2==1:
  for i in range(1,k+1):
    ans[i-1].append(i)
  for i in range(1,k+1):
    ans[i-1].append(n-i+1)
  for i in range(k):
    print(*ans[i])
else:
  if n%4==0:
    for i in range(1,k+1):
      ans[i-1].append(i)
    for i in range(1,k+1):
      if i<=k//2+1:
        ans[i-1].append(n-i+1)
      else:
        ans[i-1].append(n-i)
  else:
    for i in range(1,k+1):
      ans[i-1].append(i)
    for i in range(1,k+1):
      if i<=k//2:
        ans[i-1].append(n-i+1)
      else:
        ans[i-1].append(n-i)
  for i in range(k):
    print(*ans[i])