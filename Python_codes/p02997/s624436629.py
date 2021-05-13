n,k=map(int,input().split())
if k>(n-1)*(n-2)//2:
  print(-1)
else:
  count=0
  now=2
  ans=[]
  for i in range(2,n+1):
    ans.append([1,i])
  now1=2
  while count<(n-1)*(n-2)//2-k:
    count+=1
    now1+=1
    if now1==n+1:
      now+=1
      now1=now+1
    ans.append([now,now1])
  print(len(ans))
  for i in ans:
    print(i[0],i[1])